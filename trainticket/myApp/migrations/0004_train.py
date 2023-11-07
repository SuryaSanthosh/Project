# Generated by Django 4.2.5 on 2023-11-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=100)),
                ('train_number', models.CharField(max_length=10)),
                ('departure_station', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_station', models.CharField(max_length=100)),
                ('arrival_time', models.TimeField()),
                ('duration', models.CharField(max_length=20)),
                ('available_classes', models.CharField(max_length=100)),
            ],
        ),
    ]