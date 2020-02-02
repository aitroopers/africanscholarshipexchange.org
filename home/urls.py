from django.conf.urls import url, include
from views import *


urlpatterns = [
    url(r'about$', about, name="about"),
    url(r'$', home, name="home"),
]
