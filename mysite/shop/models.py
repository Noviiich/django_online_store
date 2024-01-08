from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', default=1)
    created_at = models.DateTimeField(default=timezone.now)
    popularity_score = models.IntegerField(default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', default='images/default.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def increase_popularity(self, amount=1):
        self.popularity_score += amount
        self.save()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username