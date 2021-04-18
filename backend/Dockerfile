# Q: Why not use ansible?
#
# A: I originally started out this project as an ansible project, but removed
#    it. I think there are several reasons why Ansible isn't a good external
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
#    4. Ansible seems to have a bug (*cough* feature) where it can only use
#       `apt` within the context of the machine's system python (not a venv), and
#       requires python3-apt (which isn't installed when ansible is installed).
#       Given that `apt` is the main task we're running, it doesn't make
#       sense to install such heavy additional libraries onto the server. We'll
#       just call `apt` directly.
#
# Ultimately, Ansible is probably too heavy for this project, especially
# because of the nature of docker here. Ansible is generally intended to be
# run on machines that remain running, and therefore the build needs to be
# repeatable without duplicating or overwriting things. In a docker container
# situation, the container is always being built from scratch -- it's fine to
# use bash commands that aren't repeatable, especially when there are so few.

FROM python:3.8.6-slim-buster

ENV PYTHONBUFFERED=1

ARG APP_DIR
COPY backend $APP_DIR
WORKDIR $APP_DIR

# Let's get building!
RUN apt-get update && \
    apt-get install -y libpq-dev build-essential

RUN pip install -U pip && \
    pip install -r requirements/server.txt
