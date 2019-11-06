from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField(max_length=100, verbose_name='Название пиццерии')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    adress = models.CharField(max_length=100, verbose_name='Адрес пиццерии')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.SET(None))
    name = models.CharField(max_length=30, verbose_name='Пицца')
    short_descriptions = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pizza_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.get_full_name()
