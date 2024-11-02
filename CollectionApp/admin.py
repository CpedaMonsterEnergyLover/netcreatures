from django.contrib import admin
from . import models as collection_models


admin.site.register(collection_models.WebsiteType)
admin.site.register(collection_models.WebsiteSignature)


@admin.register(collection_models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created']


@admin.register(collection_models.Creature)
class CreatureAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created']


@admin.register(collection_models.CreatureInstance)
class CreatureInstanceAdmin(admin.ModelAdmin):
    readonly_fields = ['date_acquired']


@admin.register(collection_models.CreatureEncounter)
class CreatureEncounterAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created']