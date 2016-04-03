from django.conf.urls import url
from SpreadSheet.views import *

__author__ = 'Saad'

urlpatterns = [
    # SpreadSheet Section
    url(r'^$', HomeView.as_view(),  name='home_view'),
]