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
from project.social.models import Social


class Command(BaseCommand):

    help = 'Add data set for testing/development'

    def handle(self, *args, **kwargs):

        print('Seeding database with some data...')

        print('adding social links and widgets')
        social = Social()
        social.title = 'Meteleska Instagram'
        social.name = 'instagram'
        social.url = 'https://instagram.com/meteleska'
        social.save()

        social = Social()
        social.title = 'Meteleska Facebook'
        social.name = 'facebook'
        social.position = 1
        social.url = 'https://facebook.com/meteleska'
        social.widget_code = '<iframe src="http://www.facebook.com/plugins/likebox.php?href=https%3A%2F%2Fwww.facebook.com%2Fmeteleska&amp;width=560&amp;colorscheme=light&amp;show_faces=true&amp;border_color=%23c0c0c0&amp;stream=true&amp;header=false&amp;height=450" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:500px; height:450px;" allowtransparency="true"></iframe>'
        social.save()

        social = Social()
        social.title = 'Meteleska Twitter'
        social.name = 'twitter'
        social.position = 3
        social.url = 'https://twitter.com/meteleska'
        social.widget_code = '<a class="twitter-timeline" data-width="560" data-height="450" href="https://twitter.com/meteleska?ref_src=twsrc%5Etfw">Tweets by meteleska</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
        social.save()

        social = Social()
        social.title = 'Meteleska Soundcloud'
        social.name = 'soundcloud'
        social.position = 2
        social.url = 'https://soundcloud.com/meteleska'
        social.save()

        social = Social()
        social.title = 'Meteleska Bandzone'
        social.name = 'bandzone'
        social.position = 4
        social.url = 'https://bandzone.cz/meteleska'
        social.save()

        social = Social()
        social.title = 'Meteleska  Youtube'
        social.name = 'youtube'
        social.position = 5
        social.url = 'https://youtube.com/user/meteleska'
        social.save()

        print('Adding superuser admin!')
        user = User()
        user.username = 'admin'
        user.email = 'dorian.podulka+a@pohodli.com'
        user.set_password('bflmpsvz313')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        print('Add some events...')
        event = Event()
        event.title = 'Koncert na Míru @ Dejvická Klubovna'
        event.datetime = timezone.now() + timedelta(days=14)
        event.location = 'Dejvická Klubovna'
        event.address = 'Generála Píky, Prague 4'
        event.slug = 'koncert-na-miru-dejvicka-klubovna'
        event.save()

        event = Event()
        event.title = 'Privat akce'
        event.datetime = timezone.now() - timedelta(days=16)
        event.location = '-'
        event.address = '-'
        event.slug = 'privat-akce'
        event.save()

        print('Seeding done.')