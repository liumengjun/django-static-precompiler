from django.test import TestCase, Client
from django.core.urlresolvers import reverse


# Create your tests here.
class TestIndex(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse('test_app:index'))
        self.assertEqual(response.status_code, 200)
        # print(response.content)
