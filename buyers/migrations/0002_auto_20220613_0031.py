# Generated by Django 3.1.4 on 2022-06-12 19:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buyer',
            new_name='Buyer_per',
        ),
    ]