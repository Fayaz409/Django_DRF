from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title_name = models.CharField(max_length=100)
    has_passport = models.BooleanField()
    salary = models.IntegerField()
    hire_date = models.DateField()
    notes = models.CharField(max_length=200)
    email = models.EmailField(default='',max_length=50)
    phone_number = models.CharField(default='',max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"