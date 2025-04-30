from django.db import models
from django.contrib.auth.models import User
from flower_shop import settings
from flowers.models import Flower 

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    delivery_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    class Meta:
        ordering = ['-order_date']

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.flower.name} for {self.user.username}"

    def total_price(self):
        return self.quantity * self.flower.price

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.flower.name}"

    def total_price(self):
        return self.quantity * self.flower.price


RIBBON_TYPE_CHOICES = [
    ('satin', 'Satin'),
    ('organza', 'Organza'),
    ('velvet', 'Velvet'),
]

class OrderCustomization(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='customizations')
    ribbon_type = models.CharField(max_length=20, choices=RIBBON_TYPE_CHOICES)
    ribbon_color = models.CharField(max_length=30)
    custom_message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ribbon_type} - {self.ribbon_color}"
