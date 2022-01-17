import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import path
from .models import *
import xlwt
from django.http import HttpResponse


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


# def response_error_handler(request, exception=None):
#     return HttpResponse('Error handler content', status=403)

# def handler500(request):
#     return render(request, '500.html', status=500)


# Create your Class views here.

class Base64PhotoView(ListView):
    model = Base64Photo
    template_name = 'Base64Photo.html'

    def download_excel_data(request):
        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header names, you can use your own headers here
        columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # get your data, from database or from a text file...
        data = Base64Photo.objects.all()  # dummy method to fetch data.
        for my_row in data:
            row_num = row_num + 1
            ws.write(row_num, 0, my_row.name, font_style)

        wb.save(response)
        return response


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
