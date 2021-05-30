from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
from shortuuidfield import ShortUUIDField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# Create your models here.

class customerentry(models.Model):
    id = ShortUUIDField(primary_key=True, default=uuid.uuid4, editable=False,max_length=6)
    Customername=models.CharField(default="user",max_length=50)
    Receivedate=models.DateField(default=datetime.now())
    Deliverydate=models.DateField(default=datetime.now())
    jobpending=models.CharField(max_length=20)
    Email=models.CharField(max_length=30,default='Trubotattend@gmail.com')

    devicebrand=models.CharField(max_length=10,default="I-Phone")
    model=models.CharField(max_length=10,default="I-Phones")
    imei=models.CharField(max_length=20)
    devicecolour=models.CharField(max_length=10,default="Black")
    providerinfo=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    fault=models.CharField(max_length=200,default="Error")
    amount=models.IntegerField(default=0)

    power=models.BooleanField(default=False)
    charging=models.BooleanField(default=False)
    display=models.BooleanField(default=False)
    camera=models.BooleanField(default=False)
    battery=models.BooleanField(default=False)
    pictures=models.ImageField(upload_to='device_images',blank=True)
    others=models.TextField(max_length=200)  
    parts=models.TextField(max_length=120,default="NOTHING YET")
    status=models.BooleanField(default=False)
    
class Mobilemodel(models.Model):
    devicename=models.CharField(max_length=100)
    def __str__(self):
        return self.devicename
class customer(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    def __str__(self):
        return self.devicename
# class CustomUser(AbstractUser):
#     username=models.CharField(primary_key=True,max_length=100,default='trubot_employee')
#     password=models.CharField(max_length=20)
#     date_of_join=models.DateField(default=datetime.now())

#     def __str__(self):
#         return self.username            