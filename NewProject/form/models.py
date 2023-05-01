from django.db import models


# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=20, null=True)
    UserName = models.CharField(max_length=20, null=True)
    CompanyName = models.CharField(max_length=30, null=True)
