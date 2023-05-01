from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=50)
    eid = models.IntegerField(max_length=4)
