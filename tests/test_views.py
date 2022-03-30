from django.test import TestCase

# Create your tests here.

from users.models import User
from django.urls import reverse

class UserListViewTest(TestCase):

    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def setUpTestData(cls):
        number_of_user = 13
        for id in range(number_of_user):
            User.objects.create(username='HDHD %s' % id, password = '1234 %s' % id,)

    def test_view_url_registration(self):
        resp = self.client.get('/registration/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/user/13/edit/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertTrue(resp.context['password'] == '1234')
        self.assertTrue( len(resp.context['users']) == 10)

    def test_lists_all_users(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.context)
        self.assertTrue(resp.context['users'] == True)
        self.assertTrue( len(resp.context['users']) == 3)