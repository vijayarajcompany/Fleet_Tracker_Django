# from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.response import Response

from rest_framework import viewsets

from tracker.models import Task, SubTask, Emirates, Employee, Department, SubDepartment
from tracker.API.serializers import TaskSerializer, SubTaskSerializer, EmiratesSerializer, EmployeeSerializer,DepartmentSerializer, SubDepartmentSerializer


# class TaskListViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskList(ListAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


class EmiratesList(ListAPIView):
    queryset = Emirates.objects.all()
    serializer_class = EmiratesSerializer


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubDepartmentList(ListAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
