from django.db import models
from buyers.models import Buyer_per
import uuid
# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer_per, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}--{self.price}--{self.buyer}"

    # simple method
    
    # def save(self, *args, **kwargs):
    #     if self.code == "":
    #         self.code = str(uuid.uuid4()).replace("_", "").upper()[:10]
    #     return super().save(*args, **kwargs)