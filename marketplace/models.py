from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    pod_customizable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



class ChatMessage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    unseen = models.BooleanField(default=True)

    def __str__(self):
        return f"To {self.user.username} | {'Admin' if self.is_admin else 'User'}: {self.message[:30]}"
    
class CustomOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    custom_text = models.CharField(max_length=200)
    custom_image = models.ImageField(upload_to='custom_orders/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name}"
