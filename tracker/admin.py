from django.contrib import admin

from . import models


# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

# class SubModelAdmin(admin.ModelAdmin):
#     list_display = ('name',)

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


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BrandSupplierAdmin(admin.ModelAdmin):
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
    list_display = ('id', 'name',)


class VehicleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'plate_no', 'emirates_id', 'platecode', 'supplier_id', 'fuelcard_id', 'brandsupplier_id',
         'type_id',
        'subdepartment_id', 'model_year', 'equipment', 'chess', 'contract_start_date',
        'contract_end_date',
        'location')


class FleetToUserAdmin(admin.ModelAdmin):
    list_display = ('id',)


class FuelCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.SubTask, SubTaskAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Emirates, EmirateAdmin)
admin.site.register(models.FuelCard, FuelCardAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.SubDepartment, SubDepartmentAdmin)
admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.VehicleType, VehicleTypeAdmin)
admin.site.register(models.Part, VehiclePartAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.BrandSupplier, BrandSupplierAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Model, ModelAdmin)
# admin.site.register(models.SubModel, SubModelAdmin)
admin.site.register(models.VehicleDetail, VehicleDetailAdmin)
admin.site.register(models.FleetToUser, FleetToUserAdmin)



