"""Test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import tracker.views
import tracker.API.views


admin.site.site_header = "Fleet Tracker Admin"
admin.site.site_title = "Fleet Tracker Admin "
admin.site.index_title = "Welcome to Fleet Tracker"
# router = DefaultRouter()
# router.register(r'tasks', tracker.API.views.TaskListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),

    # API
    # GET
    path('api/v1/users/', tracker.API.views.UserList.as_view()),
    path('api/v1/task/', tracker.API.views.TaskList.as_view()),
    path('api/v1/subtask/', tracker.API.views.SubTaskList.as_view()),
    path('api/v1/employees/', tracker.API.views.EmployeeList.as_view()),
    path('api/v1/emirates/', tracker.API.views.EmiratesList.as_view()),
    path('api/v1/department/', tracker.API.views.DepartmentList.as_view()),
    path('api/v1/subdepartment/', tracker.API.views.SubDepartmentList.as_view()),
    path('api/v1/employees/', tracker.API.views.EmployeeList.as_view()),
    path('api/v1/vehicledetail/', tracker.API.views.VehicleDetailList.as_view()),
    # GET By ID
    # /api/v1/employees/?emp_id=13578
    path('api/v1/employees/?emp_id=<int:emp_id>', tracker.API.views.EmployeeList.as_view()),
    path('api/v1/vehicledetail/?plate_no=<int:plate_no>', tracker.API.views.VehicleDetailList.as_view()),

    # /api/v1/users/?usr_name=13578
    path('api/v1/users/?name=<str:name>&password=<str:password>', tracker.API.views.UserList.as_view()),
    # POST
    path('api/v1/vehicledetail/new', tracker.API.views.VehicleDetailCreate.as_view()),
    path('api/v1/employees/new', tracker.API.views.EmployeeCreate.as_view()),

    path('api/v1/basephoto/', tracker.API.views.BasePhotoList.as_view()),
    path('api/v1/basephoto/new', tracker.API.views.BasePhotoCreate.as_view()),
    path('api/v1/binaryphoto/', tracker.API.views.BinaryPhotoList.as_view()),
    path('api/v1/binaryphoto/new', tracker.API.views.BinaryPhotoCreate.as_view()),


]



