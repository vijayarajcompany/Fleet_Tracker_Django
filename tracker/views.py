import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import path
from .models import *


# Create your Class views here.
class HomeView(ListView):
    # var1 = 0
    # var2 = 1
    model = Task
    template_name = 'home.html'
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context



class LoginView(TemplateView):
    template_name = 'mylogin.html'

# Create your views here.
# def home(request):
#     return render(request, 'home.html')
