# Generated by Django 2.2.5 on 2019-10-22 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_answer_upvotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='Upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]