# Generated by Django 4.2.5 on 2023-11-25 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='route',
            name='departure_station',
        ),
        migrations.RemoveField(
            model_name='route',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='route',
            name='intermediate_stations',
        ),
        migrations.RemoveField(
            model_name='route',
            name='train',
        ),
        migrations.AddField(
            model_name='route',
            name='destination_station',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='route',
            name='arrival_station',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='RouteDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=255)),
                ('fare_amount', models.PositiveIntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.route')),
            ],
        ),
    ]
