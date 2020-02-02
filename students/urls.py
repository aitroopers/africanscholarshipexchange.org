from django.conf.urls import url
from views import *

urlpatterns = [

    url(r'$', students, name="students"),

]
