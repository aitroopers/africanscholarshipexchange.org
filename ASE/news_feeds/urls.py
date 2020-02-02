from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'$', news_feeds, name="news_events"),
]

