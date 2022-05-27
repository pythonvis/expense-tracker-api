from django.db import models


# Create your models here.
class Expense(models.Model):
    amount = models.FloatField()
    shopname = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
