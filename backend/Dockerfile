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

COPY ansible /build

WORKDIR /build

# TODO: run this from a virtualenv in /build that can be cleaned up. We don't
# need it running on the regular server
RUN pip install -U pip && pip install ansible

RUN ansible-playbook -i hosts -e "server_role=backend" deploy.yml

# TODO: clean up build
