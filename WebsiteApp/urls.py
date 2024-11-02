from django.urls import path

from views import GetWebsiteSignature

urlpatterns = [
    path('websites/get_signature/', GetWebsiteSignature.as_view(), name="get-signature"),
]
