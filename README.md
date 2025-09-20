# Ex02 Django ORM Web Application
## Date:20/9/2025 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<WhatsApp Image 2025-09-13 at 11.18.54_6df826ef.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
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
```


## OUTPUT

Include the screenshot of your admin page.
![alt text](<Screenshot 2025-09-20 132950.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
