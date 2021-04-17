# Infrastructure Demo

This is a basic toy project to play with some infrastructure concepts in
various technologies.

The setup is as follows:

1. Frontend running a Javascript application, with public access.
2. Backend running a Python-based API; only the frontend has access.
3. Database that can be accessed only by the backend.

The actual frontend/backend code is irrelevant and is primarily just used to
test the project.

## Requirements

* Python 3.8.6
* docker and docker-compose
* postgres dev libraries for your distribution (e.g., libpq-dev)
