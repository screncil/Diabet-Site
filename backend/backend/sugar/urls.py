from django.urls import path

from .views import *

urlpatterns = [
    path("", СarbohydratesAPI.as_view())
]