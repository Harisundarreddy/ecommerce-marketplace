from django.db import models

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
    

class CustomOrder(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    custom_text = models.CharField(max_length=200)
    custom_image = models.ImageField(upload_to='custom_orders/')
    created_at = models.DateTimeField(auto_now_add=True)
