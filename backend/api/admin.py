from django.contrib import admin

from backend.api import models

admin.site.register(models.InternalData)
admin.site.register(models.User)
