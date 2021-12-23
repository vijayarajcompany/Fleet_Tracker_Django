# from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.response import Response

from rest_framework import viewsets

from tracker.models import Task
from tracker.API.serializers import TaskSerializer


# class TaskListViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
