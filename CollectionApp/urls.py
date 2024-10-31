from django.urls import path

from .views import GetEncounter, FinishEncounter

urlpatterns = [
    path('encounter/get/', GetEncounter.as_view(), name="get-encounter"),
    path('encounter/finish/', FinishEncounter.as_view(), name="finish-encounter"),
]
