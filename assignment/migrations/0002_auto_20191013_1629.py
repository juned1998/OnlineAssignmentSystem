# Generated by Django 2.2.5 on 2019-10-13 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='faculty',
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assignment.Faculty'),
        ),
    ]