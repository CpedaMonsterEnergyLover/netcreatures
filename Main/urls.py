from django.contrib import admin
from django.urls import include, path
from . views import index, profile, collection, LinkAccount
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("", include("CollectionApp.urls")),
    path("", include("WebsiteApp.urls")),

    path('profile/', profile, name="profile"),
    path('collection/', collection, name="collection"),
    path('admin/', admin.site.urls),

    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/link_account/', LinkAccount.as_view(), name="link_account")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
