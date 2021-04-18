#!/bin/bash

###############################################################################
#                                                                             #
#  Starts the server to run the django project                                #
#                                                                             #
###############################################################################

gunicorn demo_backend.asgi:application \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
