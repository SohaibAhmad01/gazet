from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
app_models = apps.get_app_config('usagazet').get_models()
for model in app_models:
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
    try:
        admin.site.register(model, ModelAdmin)
    except AlreadyRegistered:
        pass