#!/bin/bash

###############################################################################
#                                                                             #
#  Run scripts required to finish building the django project                 #
#                                                                             #
###############################################################################

pip install -r requirements/base.txt
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# TODO: script to create superuser in a safe way
