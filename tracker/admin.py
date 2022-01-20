from django.contrib import admin

from . import models


# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmirateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VehiclePartAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VehicleDetailAdmin(admin.ModelAdmin):
    list_display = ('plate_no',)


class FleetToUserAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.SubTask, SubTaskAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Emirates, EmirateAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.SubDepartment, SubDepartmentAdmin)
admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.VehicleType, VehicleTypeAdmin)
admin.site.register(models.Part, VehiclePartAdmin)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Model, ModelAdmin)
admin.site.register(models.VehicleDetail, VehicleDetailAdmin)
admin.site.register(models.FleetToUser, FleetToUserAdmin)
