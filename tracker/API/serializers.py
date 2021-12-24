from rest_framework import serializers
from tracker.models import Task,SubTask,Emirates


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
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('id', 'name', 'title')
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         return data
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('id', 'name', 'title')
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         return data
