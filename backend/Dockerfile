# Q: Why are we using ansible from within the docker container, and not
#    controlling the whole build process externally through ansible?
#
# A: I think there are several reasons why Ansible isn't a good external
#    controller here:
#
#    1. The docker `.env` file is a simple way to change variables on-the-fly
#       when doing local development, without needing to pass args on the
#       command line. Ansible is missing this even in its `docker_service`
#       command.
#
#    2. While Ansible has a `lookup` feature to get environmental variables, it
#       doesn't directly inject environmental variables into the VM the way
#       Docker can. This forces us to write passwords/secrets to files in
#       order to persist ansible's variables after the build -- files that
#       are potentially read-only to more than just the root user.
#
#    3. Ansible has a vault system to keep secrets/passwords safe, but it still
#       requires committing secrets into the code base. The encrypted format
#       means that it is more difficult to audit and change. Personally, I
#       would prefer something like AWS Secrets Manager, or even setting the
#       secret variables manually with the host service (e.g., AWS, Heroku) if
#       possible first.
#
# Ultimately, Ansible is probably too heavy for this project, especially
# because of the nature of docker here. Ansible is generally intended to be
# run on machines that remain running, and therefore the build needs to be
# repeatable without duplicating or overwriting things. In a docker container
# situation, the container is always being build from scratch -- it's fine to
# use bash commands that aren't repeatable.
#
# If I had time to go back and this were a real project, I would probably
# remove it; this is more just a showcase.
#
# TODO: unit testing ansible setup with molecule?

FROM python:3.8.6-slim-buster

ARG BUILD_DIR="/build"
ARG APP_DIR

ENV PYTHONBUFFERED=1

# Let's get building!
COPY ansible $BUILD_DIR
COPY backend $APP_DIR

WORKDIR $BUILD_DIR

RUN python3 -m venv venv && \
    venv/bin/pip install ansible && \
    venv/bin/ansible-playbook -i hosts -e "server_role=backend app_dir=$APP_DIR" deploy.yml

WORKDIR $APP_DIR

# Let's cleanup these files so they're not available on the server
RUN rm -rf $BUILD_DIR
