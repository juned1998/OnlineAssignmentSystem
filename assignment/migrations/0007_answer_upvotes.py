# Generated by Django 2.2.5 on 2019-10-22 15:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0006_auto_20191018_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(related_name='Upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
