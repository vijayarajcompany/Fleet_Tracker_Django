from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
import tracker.API.views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view()),
    path('login', views.LoginView.as_view()),
    path('photo', views.Base64PhotoView.as_view()),
]

# path('home', views.home)
# path('task', tracker.API.views.TaskList.as_view({'get': 'list'})),
# path('task', tracker.API.views.TaskList.as_view()),
