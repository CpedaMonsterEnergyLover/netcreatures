from django.contrib import admin
from django.urls import include, path
from . views import index, profile, collection

urlpatterns = [
    path("", index, name="index"),
    path("", include("CollectionApp.urls")),

    path('profile/', profile, name="profile"),
    path('collection/', collection, name="collection"),
    path('admin/', admin.site.urls),

    path('auth/', include('social_django.urls', namespace='social')),

]
