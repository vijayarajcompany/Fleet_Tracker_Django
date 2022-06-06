from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import viewsets

from tracker.models import *
from tracker.API.serializers import *


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)



class PartsList(ListAPIView):
    queryset = Part.objects.all()
    serializer_class = VehiclePartSerializer


class FleetList(ListAPIView):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer

# class UserList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class BinaryPhotoList(ListAPIView):
    queryset = BinaryPhoto.objects.all()
    serializer_class = BinaryPhotoSerializer


class BasePhotoList(ListAPIView):
    queryset = Base64Photo.objects.all()
    serializer_class = BasePhotoSerializer


class BinaryPhotoCreate(CreateAPIView):
    serializer_class = BinaryPhotoSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        binaryphoto = request.data.get('binaryphoto')
        return super().create(request, *args, **kwargs)


class BasePhotoCreate(CreateAPIView):
    serializer_class = BasePhotoSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        basephoto = request.data.get('basephoto')
        return super().create(request, *args, **kwargs)


class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskList(ListAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


class EmiratesList(ListAPIView):
    queryset = Emirates.objects.all()
    serializer_class = EmiratesSerializer

class LicenseList(ListAPIView):
    queryset = Emirates.objects.all()
    serializer_class = LicenseSerializer

class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('emp_id',)
    search_fields = ('emp_id', 'name')


class EmployeeCreate(CreateAPIView):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        emp_id = request.data.get('emp_id')
        name = request.data.get('name')
        emirates_id = request.data.get('emirates_id')
        contact_number = request.data.get('contact_number')
        active = request.data.get('active')
        return super().create(request, *args, **kwargs)


class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubDepartmentList(ListAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'password')
    search_fields = ('name',)


class FuelCardList(ListAPIView):
    queryset = FuelCard.objects.all()
    serializer_class = FuelCardSerializer


class ModelList(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class VehicleList(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BrandList(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandSupplierList(ListAPIView):
    queryset = BrandSupplier.objects.all()
    serializer_class = BrandSupplierSerializer


# class VehicleDetailList(ListAPIView):
#     queryset = VehicleDetail.objects.all()
#     serializer_class = VehicleDetailSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     filter_fields = ('plate_no',)
#     search_fields = ('plate_no',)


class VehicleDetailList(ListAPIView):
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('plate_no',)
    search_fields = ('plate_no',)


# model_id = request.data.get('model_id')

class VehicleDetailCreate(CreateAPIView):
    serializer_class = VehicleDetailSerializer

    def create(self, request, *args, **kwargs):
        plate_no = request.data.get('plate_no')
        supplier = request.data.get('supplier_id')
        fuelcard_id = request.data.get('fuelcard_id')
        brandsupplier_id = request.data.get('brandsupplier_id')
        emirates_id = request.data.get('emirates_id')
        type_id = request.data.get('type_id')
        subdepartment_id = request.data.get('subdepartment_id')
        model_year = request.data.get('ModelYear')
        equipment = request.data.get('Equipment')
        chess = request.data.get('Chess')
        platecode = request.data.get('PlateCode')
        contract_start_date = request.data.get('contract_start_date')
        contract_end_date = request.data.get('contract_end_date')
        location = request.data.get('location')
        return super().create(request, *args, **kwargs)


class FleetToUserList(ListAPIView):
    queryset = FleetToUser.objects.all()
    serializer_class = FleetToUserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('plate_number',)
    search_fields = ('plate_number',)

    def create(self, request, *args, **kwargs):
        plate_no = request.data.get('plate_no')
        emirates = request.data.get('emirates')
        plate_code = request.data.get('plate_code')
        plate_number = request.data.get('plate_number')
        km = request.data.get('km')
        fuel_tank = request.data.get('fuel_tank')
        entry_date = request.data.get('EntryDate')
        time = request.data.get('Time')
        employee_id = request.data.get('employee_id')
        parts = request.data.get('parts')
        license_code = request.data.get('license_code')
        comments = request.data.get('comments')

        return super().create(request, *args, **kwargs)
