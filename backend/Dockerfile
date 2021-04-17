# Q: Why are we using ansible from within the docker container, and not
#    controlling the whole build process externally through ansible?
#
# A: Ansible officially recommends `ansible-container[docker]` to run docker
#    builds; however `ansible-container` hasn't been maintained since at least
#    2018 and still uses pip<10.0. Downgrading pip to 9.0.3 results in being
#    unable to use the most recent version of ansible; rather than use an
#    outdated ansible, we're going to forego ansible-container and let docker
#    handle the first steps of the build.
#
#    Ansible has a long history of not keeping various projects up to date,
#    including the debacle in 2020 when they didn't support python3 until after
#    python2 was deprecated. We may want to look into other, better-maintained
#    build systems (e.g., salty vagrant?)

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
