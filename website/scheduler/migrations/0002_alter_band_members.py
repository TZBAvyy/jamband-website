# Generated by Django 5.1.4 on 2025-01-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='bands', to='scheduler.member'),
        ),
    ]
