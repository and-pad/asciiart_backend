from django.urls import path

from asciiart.views import asciiJpg

urlpatterns = [
    path("api/ascii/", asciiJpg.as_view()),
]
