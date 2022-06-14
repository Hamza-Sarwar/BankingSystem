from django.db import models

#Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100, default="ABC")
    last_name = models.CharField(max_length=100, default="Xyz")
    email = models.EmailField(max_length=100, default="haz@gmail.com")
    current_balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.first_name} | {self.email} | {self.current_balance}"
