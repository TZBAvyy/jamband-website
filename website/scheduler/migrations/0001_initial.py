# Generated by Django 5.1.4 on 2025-01-05 14:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'ordering': ['-date', '-time'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter a member's full name (e.g. Avi)", max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Member name must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
                ('band_no', models.IntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bands', to='scheduler.event')),
                ('members', models.ManyToManyField(related_name='bands', to='scheduler.member')),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practices', to='scheduler.band')),
            ],
            options={
                'ordering': ['date', 'startTime'],
            },
        ),
    ]
