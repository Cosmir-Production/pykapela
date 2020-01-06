#!/usr/bin/env python

import logging
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings
from django.core.management.base import BaseCommand
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree, register_i18n_trees, get_sitetree
from sitetree.utils import tree, item

from project.events.models import Event


class Command(BaseCommand):

    help = 'Add data set for testing/development'

    def handle(self, *args, **kwargs):

        print('Seeding database with some data...')

        superuser
        user = User()
        user.username = 'admin'
        user.email = 'dorian.podulka+a@pohodli.com'
        user.set_password('bflmpsvz313')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        event = Event()
        event.title = 'Koncert na Míru @ Dejvická Klubovna'
        event.datetime = timezone.now() + timedelta(days=14)
        event.location = 'Dejvická Klubovna'
        event.address = 'Generála Píky, Prague 4'
        event.slug = 'koncert-na-miru-dejvicka-klubovna'
        event.save()

        event = Event()
        event.title = 'Privat akce'
        event.datetime = timezone.now() + timedelta(days=16)
        event.location = '-'
        event.address = '-'
        event.slug = 'privat-akce'
        event.save()

        print('Seeding done.')