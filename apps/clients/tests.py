from http import HTTPStatus
from django.test import TestCase


class TestHomePageCase(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/clients/data/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_template_content(self):
        response = self.client.get("/clients/data/")
        self.assertTemplateUsed(response, "clients/data.html")
