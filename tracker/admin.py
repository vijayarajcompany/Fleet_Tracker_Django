from django.contrib import admin

from . import models


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmirateAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.SubTask, SubTaskAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Emirates, EmirateAdmin)
# admin.site.register(models.Task, )
