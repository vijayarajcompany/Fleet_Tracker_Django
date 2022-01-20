from rest_framework import serializers
from tracker.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class BinaryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinaryPhoto
        fields = ('name', 'binaryphoto')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class BasePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base64Photo
        fields = ('name', 'basephoto')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'title')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ('id', 'task_id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class EmiratesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emirates
        fields = ('id', 'name', 'code')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'emirates_id', 'contact_number', 'active')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'name', 'password')
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         return data

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name', 'part')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class FuelCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelCard
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class BrandSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandSupplier
        fields = ('id', 'name', 'brand_id')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = (
            'plate_no', 'supplier_id', 'fuelcard_id', 'brandsupplier_id', 'emirates_id', 'model_id', 'type_id',
            'subdepartment_id', 'model_year', 'equipment', 'chess', 'platecode', 'contract_start_date',
            'contract_end_date',
            'location')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class FleetToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetToUser
        fields = (
        'id', 'plate_no', 'emirates', 'plate_code', 'km', 'fuel_tank', 'entry_date', 'time', 'employee_id', 'parts',
        'license_code', 'comments')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
