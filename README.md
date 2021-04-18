# Infrastructure Demo

This is a basic toy project to play with some infrastructure concepts in
various technologies.

The setup is as follows:

1. Frontend running a Javascript application, with public access.
2. Backend running a Python-based API; reverse proxy to the backend through the
   frontend
3. Database used by the backend

In a real project, we would probably want to separate out the frontend and
backend into their own repositories, but since this is a toy project it makes
sense to keep them together for demo purposes.

The actual frontend/backend code is irrelevant and is primarily just used to
test the project, with the exception of:

* `scripts` folder in the backend project
* `create_default_superuser` management task in the backend project


## Requirements

* Python 3.8.6
* docker and docker-compose
* postgres dev libraries for your distribution (e.g., libpq-dev)


## Quick-Start

```bash
source run-dev.sh
```


## More to Do

There was limited time to put this project together, and you'll see TODOs
scattered throughout the code. Here are some of the things I would like to have
done if I had more time:

* Implement HTTPS in the local dev environment

* Add some integration with AWS, both with boto in the django project, and
  with orbs in circleci; perhaps deploy the project somewhere.

* Build a more sophisticated frontend app that could be build using webpack or
  similar.

* Slack integration for circleci for build notices

* Add some pre-commit hooks that would run linting, isort, etc.

* Better test coverage in the backend app
