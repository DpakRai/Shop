from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
#from store.api.views import Categorylist,Categorydetail,Customerlist,Customerdetail
from store.api import views
from store.api import views as api_views
from store.api.views import *

#app_name = 'store'

urlpatterns = [
   # path('', views.snippet_list),
    path('category/',api_views.Categorylist.as_view(), name="Categorylist"),
    path("category/<int:pk>/",views.Categorydetail.as_view(),name="categorydetail"),
    path('customerlist/',Customerlist.as_view(), name="customerlist"),
    path("customerdetail/<int:pk>/",views.Customerdetail.as_view(),name="customerdetail"),
    path('orderlist/',Orderlist.as_view(), name="orderlist"),
    path("orderdetail/<int:pk>/",views.Orderdetail.as_view(),name="orderdetail"),
    path('productlist/',Productlist.as_view(), name="productlist"),
    path("productdetail/<int:pk>/",views.Productdetail.as_view(),name="productdetail"),

]



