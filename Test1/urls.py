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
    path('api/v1/task/', tracker.API.views.TaskList.as_view()),
    path('api/v1/subtask/', tracker.API.views.SubTaskList.as_view()),
    path('api/v1/employees/', tracker.API.views.EmployeeList.as_view()),
    path('api/v1/emirates/', tracker.API.views.EmiratesList.as_view()),
    path('api/v1/department/', tracker.API.views.DepartmentList.as_view()),
    path('api/v1/subdepartment/', tracker.API.views.SubDepartmentList.as_view()),
]

