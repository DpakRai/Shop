from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from store.models import category,customer,orders,product
from django.contrib.auth.models import User
import json
from store.views.login import Login
from mixer.backend.django import mixer



class TestLoginViews(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client =  Client()
        self.login_url = reverse('login')

    def test_login_list_GET(self):
        # Issue a GET request.
        response = self.client.get(self.login_url)

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, 200)

        # Check that the rendered context
        self.assertTemplateUsed(response,'login.html')


class TestSignupViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.signup_url = reverse('signup')

    def test_Signup_list_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'signup.html')


class TestStoreViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.store_url = reverse('store')

    def test_Store_list_GET(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

  


