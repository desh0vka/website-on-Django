from django.test import TestCase

# Create your tests here.

from users.models import User

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(username='Big', password='1234')

    def test_username_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'имя пользователя')

    def test_username_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length,150)

    def test_object_name_is_username_comma_password(self):
        user=User.objects.get(id=1)
        expected_object_name = '%s' % (user.username)
        self.assertEquals(expected_object_name,str(user))

    #def test_get_absolute_url(self):
        #user=User.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        #self.assertEquals(user.get_absolute_url(),'/user/1')