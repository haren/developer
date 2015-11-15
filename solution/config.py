#!/bin/env python

# when running in docker container this needs to be changed to the
# docker VM IP, e.g. on Mac can be looked up (depeneding on the used tool) using:
# docker-machine ip dev
# or
# boot2docker ip
HOST = "127.0.0.1" # localhost - "127.0.0.1", boot2docker on mac: "192.168.59.103"

# Api listening port
PORT = 8888

# CSV paths
MAIN_CSV_PATH   = "./assets/"
RATES_FILE_NAME = "rates.csv"

# Response codes
RESPONSE_ERROR         = 500
RESPONSE_NOTFOUND      = 404
RESPONSE_OK            = 200