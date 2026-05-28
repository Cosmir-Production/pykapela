from django.test import TestCase, override_settings
from django.utils import timezone

from pykapela.events.models import Event
from pykapela.pages.models import Page


@override_settings(SITE_URL_FULL='https://www.example.com')
class SeoEndpointTests(TestCase):
    def setUp(self):
        Page.objects.create(
            title='Bio',
            slug='bio',
            is_published=True,
        )
        Event.objects.create(
            title='Test show',
            slug='test-show',
            datetime=timezone.now(),
            location='Prague',
            is_published=True,
        )

    def test_robots_txt_includes_sitemap_url(self):
        response = self.client.get('/robots.txt')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Type'].startswith('text/plain'))
        self.assertIn('Sitemap: https://www.example.com/sitemap.xml', response.content.decode('utf-8'))

    def test_sitemap_xml_lists_language_variants(self):
        response = self.client.get('/sitemap.xml')
        content = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Type'].startswith('application/xml'))
        self.assertIn('<loc>https://www.example.com/cs/</loc>', content)
        self.assertIn('hreflang="en" href="https://www.example.com/en/"', content)
        self.assertIn('hreflang="x-default" href="https://www.example.com/cs/"', content)
        self.assertIn('<loc>https://www.example.com/cs/bio/</loc>', content)
        self.assertIn('<loc>https://www.example.com/cs/concerts/test-show/</loc>', content)
