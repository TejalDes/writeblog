from django.urls import path
from blogs.views import *

urlpatterns = [
    path("", ViewAll.as_view()),
    path("id/", ViewOne.as_view()),
]
