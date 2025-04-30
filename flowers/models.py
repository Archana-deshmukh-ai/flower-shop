from django.db import models
 
class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')
    is_bestseller = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_budget = models.BooleanField(default=False)

    def __str__(self):
        return self.name
 






