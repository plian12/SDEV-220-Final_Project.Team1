from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# The `Customer` class defines a model with fields for user, name, email, and points.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number= models.CharField(max_length=10, blank=True, null=True)
    points = models.IntegerField(default=0)

# The `MenuItem` class defines attributes for a menu item including name, description, and price.

class MenuItem(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    points_value = models.IntegerField(default=0)

# The Order class represents an order made by a customer, containing multiple items and the date of
# the order.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    items = models.ManyToManyField(MenuItem, related_name='orders')
    date = models.DateTimeField(default=timezone.now)

    