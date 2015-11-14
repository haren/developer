#!/bin/env python

import os
import tornado.ioloop
import tornado.httpserver
import tornado.escape
import tornado.web
import json
from tornado.options import define, options, parse_command_line

import config
import csv_handler
import currency_handler

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/rate/(?P<curr_from>[^\/]*)/(?P<curr_to>[^\/]*)", ExchangeRateHandler),
            (r".*", DefaultHandler)
        ]

        settings = dict(
            template_path=os.path.dirname(__file__),
            static_path=os.path.dirname(__file__),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class AjaxResponse(object):
    """ Base class for forming responses
    status(code) 			to set status
    add_msg(str) 			to add a text message to response
    add_field(name, value) 	to add a name/value pair to json response
    """

    def __init__(self, status=0):
        self.response = {}
        self.response['status'] = status

    def get(self):
        return self.response

    def add_code(self, code):
    	self.add_field('status', code)

    def add_msg(self, msg):
        self.add_field('msg', msg)

    def add_field(self, name, value):
        self.response[name] = value


class BaseHandler(tornado.web.RequestHandler):

    SUPPORTED_METHODS = ("GET")

    def write(self, *args, **kwargs):
        # set correct header type
        self.set_header("Content-Type", "application/json")
        super(BaseHandler, self).write(*args, **kwargs)


class ExchangeRateHandler(BaseHandler):

    def get(self, curr_from, curr_to):
        try:
            response = AjaxResponse()

            if not currency_handler.is_currency_supported(curr_from):
                response.add_code(config.RESPONSE_ERROR)
                response.add_msg('Currency %s not supported.' % curr_from)
                return # move  to finally block

            if not currency_handler.is_currency_supported(curr_to):
                response.add_code(config.RESPONSE_ERROR)
                response.add_msg('Currency %s not supported.' % curr_to)
                return # move  to finally block

            rate = currency_handler.get_currencies_exchange_rate(curr_from, curr_to)
            response.add_code(config.RESPONSE_OK)
            response.add_field('rate', rate)

        except Exception, e:
            response.add_code(config.RESPONSE_ERROR)
            response.add_msg('Internal Error')

        finally:
            response = tornado.escape.json_encode(
            	response.get())
            self.write(response)
            self.finish()


class DefaultHandler(BaseHandler):

    def get(self):
        try:
            response = AjaxResponse()
            response.add_code(config.RESPONSE_NOTFOUND)
            response.add_msg("Incorrect request url.")

        except Exception, e:
        	print e
        	response.add_code(config.RESPONSE_ERROR)
        	response.add_msg('Internal Error')

        finally:
            response = tornado.escape.json_encode(
            	response.get())
            self.write(response)
            self.finish()


if __name__ == '__main__':

    csv_handler = csv_handler.CsvHandler(
        './assets', 'rates.csv')
    currency_handler = currency_handler.CurrencyHandler(
        csv_handler.get_csv_data())

    http_server = tornado.httpserver.HTTPServer(Application())
    # TODO PASS PORT FROM CONFIG
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()