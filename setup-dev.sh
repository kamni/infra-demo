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
###############################################################################

if [ ! -d ".venv" ]; then
    echo "[setup-dev] Creating virtual env for the first time..."
    python3 -m venv .venv

    echo "[setup-dev] Installing requirements..."
    pip install --upgrade pip
    pip install -r requirements/dev.txt
fi
source .venv/bin/activate
