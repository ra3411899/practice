# from django.contrib import admin
# from django.urls import path, include
# from .views import index

# urlpatterns = [
#     path("", index, name= "home"),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]

