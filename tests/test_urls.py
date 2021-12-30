from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.views import  View
from store.api.urls import *
from rest_framework import status
from rest_framework.test import  APITestCase
from store.views.signup import Signup
from store.views.login import Login,logout
from store.views.home  import Index, store
from store.views.checkout import CheckOut
from store.api import views
#from rest_framework.test import APITestcase

class TestUrls(SimpleTestCase):

    #Hompage url 
    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func.view_class,Index)

    #Store url 
    def test_store_url_is_resolved(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func,store)
    

    #signup url 
    def test_Signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class,Signup)


    #Login url 
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class,Login)

    
    #Logout url 
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logout)

    #Checkout url 
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func.view_class,CheckOut)


    #API URL TEST
    #Categorylist url 
    def test_Categorylist_url_is_resolved(self):
        url = reverse('Categorylist')
        self.assertEquals(resolve(url).func.view_class,Categorylist)


    #Categorydetail url 
    def test_Categorydetail_url_is_resolved(self):
        url = reverse('categorydetail',args=[1,])
        self.assertEquals(resolve(url).func.view_class,Categorydetail)

    
    #Customerlist url 
    def test_Customerlist_url_is_resolved(self):
        url = reverse('customerlist')
        self.assertEquals(resolve(url).func.view_class,Customerlist)

    
    #Customerdetail url 
    def test_Categorydetail_url_is_resolved(self):
        url = reverse('customerdetail',args=[1,])
        self.assertEquals(resolve(url).func.view_class,Customerdetail)

    
    #Orderlist url 
    def test_Orderlist_url_is_resolved(self):
        url = reverse('orderlist')
        self.assertEquals(resolve(url).func.view_class,Orderlist)

    #Orderdetail url 
    def test_Orderdetail_url_is_resolved(self):
        url = reverse('orderdetail',args=[1,])
        self.assertEquals(resolve(url).func.view_class,Orderdetail)

    #Orderlist url 
    def test_Productlist_url_is_resolved(self):
        url = reverse('productlist')
        self.assertEquals(resolve(url).func.view_class,Productlist)

     #Productdetail url 
    def test_Productdetail_url_is_resolved(self):
        url = reverse('productdetail',args=[1,])
        self.assertEquals(resolve(url).func.view_class,Productdetail)