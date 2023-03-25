# Generated by Django 4.1.7 on 2023-03-25 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название датчика')),
                ('description', models.CharField(max_length=100, verbose_name='Описание датчика')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Температура')),
                ('date_measure', models.DateField(auto_now_add=True, verbose_name='Дата измерения')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение с датчика')),
                ('id_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='ID датчика')),
            ],
        ),
    ]
