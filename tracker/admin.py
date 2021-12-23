from django.contrib import admin

from . import models


# Register your models here.
class FleetAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(models.Task, FleetAdmin)
