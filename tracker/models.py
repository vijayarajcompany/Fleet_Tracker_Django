from django.db import models
import base64


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FuelCard(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BrandSupplier(models.Model):
    name = models.CharField(max_length=50)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brands")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BinaryPhoto(models.Model):
    name = models.CharField(max_length=100)
    binaryphoto = models.BinaryField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Base64Photo(models.Model):
    name = models.CharField(max_length=100)
    basephoto = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubTask(models.Model):
    name = models.CharField(max_length=200)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Emirates(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subdepartments")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.PositiveIntegerField(primary_key=True)
    emirates_id = models.PositiveIntegerField(unique=True, null=False)
    name = models.CharField(max_length=100)
    contact_number = models.PositiveIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    part = models.ManyToManyField('Part')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle")
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="model", null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VehicleDetail(models.Model):
    plate_no = models.PositiveIntegerField(primary_key=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="suppliers")
    fuelcard_id = models.ForeignKey(FuelCard, on_delete=models.CASCADE, related_name="fuelcards")
    brandsupplier_id = models.ForeignKey(BrandSupplier, on_delete=models.CASCADE, related_name="brands")
    emirates_id = models.ForeignKey(Emirates, on_delete=models.CASCADE, related_name="emirates")
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="models")
    type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name="vehicletype")
    subdepartment_id = models.ForeignKey(SubDepartment, on_delete=models.CASCADE, related_name="subdepartment")
    model_year = models.CharField(max_length=4)
    equipment = models.CharField(max_length=30)
    chess = models.CharField(max_length=50)
    platecode = models.CharField(max_length=10)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    location = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate_number


class FleetToUser(models.Model):
    # subtask_id = models.ForeignKey(SubTask, on_delete=models.CASCADE, related_name="subtasks")
    plate_no = models.PositiveIntegerField()
    emirates = models.JSONField()
    plate_code = models.JSONField()
    km = models.CharField(max_length=10)
    fuel_tank = models.CharField(max_length=50)
    entry_date = models.DateField()
    time = models.TimeField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee")
    parts = models.JSONField()
    license_code = models.JSONField()
    comments = models.TextField()


class FleetToUserImage(models.Model):
    takeover_id = models.ForeignKey(FleetToUser, on_delete=models.CASCADE, related_name="takeover")
    image_name = models.CharField(max_length=100)
    takeover_image = models.TextField()
