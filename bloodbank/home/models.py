from django.db import models

# Create your models here.
class Donar(models.Model):
    firstname=models.CharField((""), max_length=50)
    lastname=models.CharField((""), max_length=50)
    age=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    pno=models.CharField((""), max_length=50)
    gender=models.CharField((""), max_length=50)
    isftd=models.CharField((""), max_length=50)
    bloodgroup=models.CharField((""), max_length=50)
    address=models.CharField((""), max_length=50)
    city=models.CharField((""), max_length=50)
    pincode=models.CharField((""), max_length=50)
    state=models.CharField((""), max_length=50)
    def __str__(self):
        return self.firstname

class Recipient(models.Model):
    firstname=models.CharField((""), max_length=50)
    lastname=models.CharField((""), max_length=50)
    age=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    pno=models.CharField((""), max_length=50)
    gender=models.CharField((""), max_length=50)
    bloodgroup=models.CharField((""), max_length=50)
    address=models.CharField((""), max_length=50)
    city=models.CharField((""), max_length=50)
    pincode=models.CharField((""), max_length=50)
    state=models.CharField((""), max_length=50)

