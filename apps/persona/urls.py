from django.conf.urls import url, include
from django.contrib import admin
from views import principal

urlpatterns = [
    url(r'^principal/', principal),
]