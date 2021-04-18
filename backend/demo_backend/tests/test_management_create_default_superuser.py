# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

# These variables are set in tox.ini
EXPECTED_EMAIL = 'test@test.local'
EXPECTED_PASSWORD = 'testpassword'


class CreateConnectorSuperuserTest(TestCase):
    """
    Tests for demo_backend.management.commands.create_default_superuser
    """

    def test_new_superuser(self):
        # Should create a superuser with the expected credentials
        user_model = get_user_model()
        call_command('create_default_superuser')

        su = user_model.objects.get(is_superuser=True)

        self.assertEqual(su.username, EXPECTED_EMAIL)
        self.assertEqual(su.email, EXPECTED_EMAIL)
        self.assertTrue(su.check_password(EXPECTED_PASSWORD))

    def test_existing_superuser(self):
        # Should update the existing superuser
        user_model = get_user_model()
        user_model.objects.create_superuser(
            EXPECTED_EMAIL,
            EXPECTED_EMAIL,
            'another-password',
        )

        call_command('create_default_superuser')

        # Verify MultipleObjectsReturned is not raised.
        sus = user_model.objects.filter(is_superuser=True)
        su = sus.first()

        self.assertEqual(sus.count(), 1)
        self.assertEqual(su.username, EXPECTED_EMAIL)
        self.assertEqual(su.email, EXPECTED_EMAIL)
        self.assertTrue(su.check_password(EXPECTED_PASSWORD))

    def test_existing_superuser_not_replaced_if_different_user(self):
        # Should update the existing superuser
        user_model = get_user_model()
        user_model.objects.create_superuser(
            'some-email@foo.com',
            'some-email@foo.com',
            'another-password',
        )

        call_command('create_default_superuser')

        # Verify MultipleObjectsReturned is not raised.
        sus = user_model.objects.filter(is_superuser=True)

        self.assertEqual(sus.count(), 2)

    def test_missing_email(self):
        # TODO: install mock and write test
        pass

    def test_missing_password(self):
        # TODO: install mock and write test
        pass

    def test_missing_email_and_password(self):
        # TODO: install mock and write test
        pass
