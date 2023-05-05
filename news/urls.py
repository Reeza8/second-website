from django.urls import path,include
from news.views import *
from news.feeds import LatestEntriesFeed

app_name='news'

urlpatterns = [
    path('',home,name='home'),
    path('category/<str:category>',category,name='category'),
    path('category/date/<str:date>',category,name='category'),
    path('search/',search,name='search'),
    path('contact/',contact,name='contact'),
    path('single/<int:id>',single_new,name='single'),
    path("rss/feed/", LatestEntriesFeed()),
    path('signup/', signup, name='signup'),
]