import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = (
        'Create a django superuser noninteractively. For use in server setup '
        'to ensure that at least one admin user is present.\n\n'
        'Please set the following environment variables:\n\n'
        '\t* DJANGO_SUPERUSER_EMAIL\n'
        '\t* DJANGO_SUPERUSER_PASSWORD\n\n'
        'The email is also used as the username for login.'
    )

    def handle(self, *args, **options):
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        if not (email and password):
            raise CommandError(
                'Missing one or both of the required environment variables: '
                'DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD',
            )

        user_model = get_user_model()

        with transaction.atomic():
            try:
                user = user_model.objects.select_for_update().get(username=email)
                user.set_password(password)
                user.email = email
                user.save()
            except user_model.DoesNotExist:
                user = user_model.objects.create_superuser(
                    username=email,
                    email=email,
                    password=password,
                )
