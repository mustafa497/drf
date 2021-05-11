from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=200, null=True, blank=True)
    optin = models.BooleanField(default=False)
    userid = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return self.userid