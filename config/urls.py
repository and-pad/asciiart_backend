from django.urls import path

from asciiart.views import asciiJpg

urlpatterns = [
    path("ascii/", asciiJpg.as_view()),
    path("api/ascii/", asciiJpg.as_view()),
]
