from django.db import models

# Create your models here.

class BiowasteModel(models.Model):
    name=models.CharField(max_length=100)
    wastetype=models.CharField(max_length=100,null=True)
    weight=models.IntegerField()
    phonenum=models.IntegerField(null=True)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()


class NonbiowasteModel(models.Model):
    name=models.CharField(max_length=100)
    wastetype=models.CharField(max_length=100, null=True)
    weight=models.IntegerField()
    phonenum=models.IntegerField(null=True)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()


class HazardouswasteModel(models.Model):
    name=models.CharField(max_length=100)
    wastetype=models.CharField(max_length=100, null=True)
    weight=models.IntegerField()
    phonenum=models.IntegerField(null=True)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()


