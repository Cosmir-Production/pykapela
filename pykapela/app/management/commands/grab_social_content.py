from datetime import datetime
from io import BytesIO
import requests

from django.core.management import BaseCommand
from django.template.defaultfilters import slugify
from django.core import files
from django.conf import settings

from pykapela.lib.instagram import *

from photologue.models import Photo, Gallery

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Run periodically to grab new Instagram data.'

    def handle(self, *args, **options):

        logger.info("Grabbing data from Instagram...")
        profile = instagram_profile_obj(settings.INSTAGRAM_PROFILE_NAME)

        try:
            edges = profile['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

        except KeyError:
            logger.exception("path to profile media not found")

        # gallery
        try:
            gallery = Gallery.objects.get(pk=1)
        except Gallery.DoesNotExist:
            gallery = Gallery(
                title='Latest',
                slug='latest',
            )
            gallery.save()

        for image in edges:
            if not image['node']['is_video']:

                bigest_photo = image['node']['thumbnail_resources'][len(image['node']['thumbnail_resources'])-1]['src']

                new_image = Photo()

                try:
                    text = image['node']['edge_media_to_caption']['edges'][0]['node']['text']
                except Exception as e:
                    continue

                logger.info("Found image %s" % text[0:settings.INSTAGRAM_TITLE_MAX_CHARS])

                # do we have already this photo?
                try:
                    photo_exists = Photo.objects.get(slug=slugify(text[0:settings.INSTAGRAM_TITLE_MAX_CHARS]))

                    # we do not update existing media
                    if photo_exists:
                        continue

                except Photo.DoesNotExist:
                    pass

                new_image.title = text[0:settings.INSTAGRAM_TITLE_MAX_CHARS]
                new_image.caption = text if text[0:settings.INSTAGRAM_TITLE_MAX_CHARS] != text else ''
                new_image.slug = slugify(text[0:settings.INSTAGRAM_TITLE_MAX_CHARS])
                new_image.date_taken = datetime.fromtimestamp(image['node']['taken_at_timestamp'])

                # grab the file and try to save:
                try:
                    resp = requests.get(bigest_photo)
                    fp = BytesIO()
                    fp.write(resp.content)
                    file_name = slugify(text[0:settings.INSTAGRAM_TITLE_MAX_CHARS])
                    new_image.image.save(file_name, files.File(fp))
                    new_image.save()  # is this necessary?
                except Exception as e:
                    continue

                gallery.photos.add(new_image)
