#!/bin/bash

###############################################################################
#                                                                             #
# Environment setup for development work                                      #
#                                                                             #
# Source this file instead of executing it.                                   #
#                                                                             #
# This requires the following already installed on the dev machine:           #
#                                                                             #
#   1. Python3 (tested with 3.8.6)                                            #
#   2. docker, docker-compose                                                 #
#                                                                             #
# #TODO: mkcert and dev domain in /etc/hosts so we can test TLS locally?      #
#                                                                             #
###############################################################################

# Although we're using docker containers, it's much easier to run and debug
# tests from a local setup. We'll set up a python virtual env here
if [ ! -d ".venv" ]; then
    echo "[setup-dev] Creating virtual env for the first time..."
    python3 -m venv .venv

    echo "[setup-dev] Installing requirements..."
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements/dev.txt
else
    source .venv/bin/activate
fi

# You can edit the .env file for more local variables to pass to your setup
if [ ! -f ".env" ]; then
    echo "[setup-dev] Creating an .env file..."
    cp .env.example .env
fi
set -a; source .env; set +a

echo "[setup-dev] Starting docker..."
docker-compose up -d
