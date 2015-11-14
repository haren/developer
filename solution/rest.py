#!/bin/env python

import os
import tornado.ioloop
import tornado.httpserver
import tornado.escape
import tornado.web

import config
import csv_handler
import currency_handler
import logger

##############################################################################
# MAIN APPLICATION CLASS
##############################################################################

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/rate/(?P<curr_from>[^\/]*)/(?P<curr_to>[^\/]*).*", ExchangeRateHandler),
            (r".*", DefaultHandler)
        ]

        settings = dict(
            template_path=os.path.dirname(__file__),
            static_path=os.path.dirname(__file__),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

##############################################################################
# BASE RESPONSE CLASS
##############################################################################

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

##############################################################################
# HANDLERS
##############################################################################

class BaseHandler(tornado.web.RequestHandler):

    SUPPORTED_METHODS = ("GET")

    def write(self, *args, **kwargs):
        # set correct header type
        main_logger.debug("Writing %s." % args)
        self.set_header("Content-Type", "application/json")
        super(BaseHandler, self).write(*args, **kwargs)


class ExchangeRateHandler(BaseHandler):

    def get(self, curr_from, curr_to):
        try:
            response = AjaxResponse()
            main_logger.debug("Requested exchange rate for %s and %s." % (curr_from, curr_to))

            if not main_currency_handler.is_currency_supported(curr_from):
                response.add_code(config.RESPONSE_ERROR)
                response.add_msg('Currency %s not supported.' % curr_from)
                return # move  to finally block

            if not main_currency_handler.is_currency_supported(curr_to):
                response.add_code(config.RESPONSE_ERROR)
                response.add_msg('Currency %s not supported.' % curr_to)
                return # move  to finally block

            # obtain and format the rate - Decimal is not json-serializable
            rate = main_currency_handler.get_currencies_exchange_rate(curr_from, curr_to)
            # assumed 6 precision points
            rate = "%.6f" % (rate)

            response.add_code(config.RESPONSE_OK)
            response.add_field('rate', rate)

        except Exception, e:
            main_logger.exception("Rest server exception: %s" % e)
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
            if 'favicon' not in self.request.uri:
                # favicon requests often come down from browsers
                main_logger.warning("Incorrect url requested.")
                response.add_msg("Incorrect request url.")

            response.add_code(config.RESPONSE_NOTFOUND)

        except Exception, e:
        	main_logger.exception("Rest server exception: %s" % e)
        	response.add_code(config.RESPONSE_ERROR)
        	response.add_msg('Internal Error')

        finally:
            if 'favicon' not in self.request.uri:
                response = tornado.escape.json_encode(
                	response.get())
                self.write(response)
                self.finish()

##############################################################################
# MAIN APPLICATION
##############################################################################

if __name__ == '__main__':

    global main_logger
    main_logger = logger.init_logger('main')

    global main_csv_handler
    main_csv_handler = csv_handler.CsvHandler(
        config.MAIN_CSV_PATH, config.RATES_FILE_NAME, main_logger)

    global main_currency_handler
    main_currency_handler = currency_handler.CurrencyHandler(
        main_csv_handler.get_csv_data(), main_logger)

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(config.PORT)
    main_logger.debug("Application initialized.")
    tornado.ioloop.IOLoop.instance().start()