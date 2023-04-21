from django.urls import path,include
from news.views import *

app_name='news'

urlpatterns = [
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('single/',single_new,name='single'),
]