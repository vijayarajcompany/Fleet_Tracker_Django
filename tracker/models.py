from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class SubTask(models.Model):
    name = models.CharField(max_length=200)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    created = models.DateTimeField(auto_now_add=True)


class Emirates(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class SubDepartment(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subdepartments")
    created = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    emp_id = models.SmallIntegerField()
    emirates_id = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    contact_number = models.SmallIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

# class Vehicle(models.Model):
#     name = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)


# taskid = models.IntegerField()
