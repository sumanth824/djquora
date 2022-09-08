# Generated by Django 4.1 on 2022-09-08 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djapp', '0009_answervote'),
    ]

    operations = [
        migrations.AddField(
            model_name='answervote',
            name='voted_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
