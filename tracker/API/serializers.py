from rest_framework import serializers
from tracker.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'title')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


