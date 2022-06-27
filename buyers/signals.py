from django.db.models.signals import post_save  # sender
from django.dispatch import receiver  # recever decorater
from django.contrib.auth.models import User
from buyers.models import Buyer_per


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        Buyer_per.objects.create(user=instance)
