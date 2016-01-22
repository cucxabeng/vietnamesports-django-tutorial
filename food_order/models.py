from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime
# Create your models here.

@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Food(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='Order')

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=datetime.now)
    # test = models.IntegerField(default=0)
