from django.db.models.signals import pre_save, post_save # post_save is more popular
from django.dispatch import receiver
from buyers.models import Buyer_per
from .models import Car
import uuid

# @receiver(pre_save, sender=Car)
# def pre_save_create_code(sender, instance, **kwargs):
#     if instance.code == "":
#         instance.code = str(uuid.uuid4()).replace("_","").upper()[:10]
        
#     obj = Buyer_per.objects.get(user=instance.buyer.user)
#     obj.from_signal = True
#     obj.save() 


@receiver(post_save, sender=Car)
def post_save_create_code(sender, created,  instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("_", "").upper()[:10]
        instance.save() # in post_save to save the object

    obj = Buyer_per.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()
