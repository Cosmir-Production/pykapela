from io import BytesIO
import requests

from django.core.management import BaseCommand
from django.template.defaultfilters import slugify
from django.core import files

from project.lib.instagram import *

from photologue.models import Photo

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Run periodically to grab new Instagram data.'

    def handle(self, *args, **options):

        profile = instagram_profile_obj('meteleska')

        try:
            edges = profile['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

        except KeyError:
            logger.exception("path to profile media not found")

        for image in edges:
            if not image['node']['is_video']:
                bigest_photo = image['node']['thumbnail_resources'][len(image['node']['thumbnail_resources'])-1]['src']

                new_image = Photo()

                try:
                    text = image['node']['edge_media_to_caption']['edges'][0]['node']['text']
                except Exception as e:
                    continue

                # do we have already this photo?
                try:
                    Photo.objects.get(slug=slugify(text[0:15]))
                except Photo.DoesNotExist:
                    pass

                new_image.title = slugify(text[0:15])
                new_image.caption = text if text[0:15] != text else ''
                new_image.slug = slugify(text[0:15])

                # grab the file and try to save:
                try:
                    resp = requests.get(bigest_photo)
                    fp = BytesIO()
                    fp.write(resp.content)
                    file_name = 'image name'
                    new_image.image.save(file_name, files.File(fp))
                    new_image.save()  # is this necessary?
                except Exception as e:
                    continue



