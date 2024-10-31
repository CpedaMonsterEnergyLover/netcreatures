from django.urls import path

from .views import get_encounter, finish_encounter

urlpatterns = [
    path('encounter/get/', get_encounter, name="get-encounter"),
    path('encounter/finish/', finish_encounter, name="finish-encounter"),
]
