from django.contrib import admin
from . import models

admin.site.register(models.Programme)
admin.site.register(models.Event)
admin.site.register(models.House)
admin.site.register(models.Student)