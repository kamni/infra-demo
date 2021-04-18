#!/bin/bash

###############################################################################
#                                                                             #
#  Starts the server to run the django project                                #
#                                                                             #
###############################################################################

function usage {
  echo "./$(basename $0) [-b]"
  echo "Include the -b flag to also build the project."
}

while getopts ":b" arg; do
  case $arg in
    b)
      scripts/build.sh
      ;;
    ?)
      echo "Invalid option."
      usage
      exit 1
      ;;
  esac
done

exec gunicorn demo_backend.asgi:application \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
