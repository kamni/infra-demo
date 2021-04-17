# Q: Why are we using ansible from within the docker container, and not
#    controlling the whole build process externally?
#
# A: Ansible has a long history of lagging behind in its development -- e.g.,
#    when Ansible didn't support Python3 until after Python2 was deprecated.
#    In this particular case, Ansible officially recommends `ansible-container`
#    to provision docker containers, but `ansible-container` has not been
#    maintained since at least 2018 and doesn't support pip >= 10; this lag
#    in development also means that you can't use `ansible-container` with the
#    most recent version of Ansible.
#
#    Therefore, we're skipping the use of `ansible-container` and relying on
#    docker to get us to the point of using ansible
#
# TODO: consider an alternative, like salty vagrant or something else that is
# better maintained.
#
# TODO: unit testing ansible setup with molecule?

FROM python:3.8.6-slim-buster

ARG BUILD_DIR="/build"
ARG APP_DIR="/opt/jleadbetter/demo"

ENV PYTHONBUFFERED=1

COPY ansible $BUILD_DIR
COPY backend $APP_DIR

WORKDIR $BUILD_DIR

RUN python3 -m venv venv && \
    venv/bin/pip install ansible && \
    venv/bin/ansible-playbook -i hosts -e "server_role=backend app_dir=$APP_DIR" deploy.yml

WORKDIR $APP_DIR

# Let's cleanup these files so they're not available on the server
RUN rm -rf $BUILD_DIR
