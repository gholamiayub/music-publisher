from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    @classmethod
    def setUpClass(self):
        self.client = Client()

    def test_home_page_status_code(self):
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.clinet.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTests(SimpleTestCase):

    @classmethod
    def setUpClass(self):
        self.client = Client()

    def test_about_page_status_code(self):
        response = self.client.get('127.0.0.1:8000/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.clinet.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
