from django.db import models

# Create your models here.
class Car(models.Model):
    #Car class is going to have an automated created pk 
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    #String representation
    def __str__(self):
        return f"The car is a {self.brand} {self.year}"