from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_ID = models.IntegerField(-)
    model = models.CharField(max_length=100)
    year = models.DateField()
    brand = models.CharField(max_length=50)
    price = models.IntegerField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_ID','model','year','brand','price')

