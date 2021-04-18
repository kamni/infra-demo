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
