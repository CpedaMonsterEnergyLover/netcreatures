from django.contrib import admin
from . import models as websites_models


@admin.register(websites_models.WebsiteType)
class WebsiteTypeAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "description"
    ]


@admin.register(websites_models.WebsiteSignature)
class WebsiteSignatureAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "type",
        "accessed"
    ]