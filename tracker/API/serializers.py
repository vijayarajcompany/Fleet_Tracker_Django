from rest_framework import serializers
from tracker.models import Task, SubTask, Emirates, Employee, Department, SubDepartment


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
        fields = ('id', 'name', 'emirates_id', 'contact_number', 'active')

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
        model = Department
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
