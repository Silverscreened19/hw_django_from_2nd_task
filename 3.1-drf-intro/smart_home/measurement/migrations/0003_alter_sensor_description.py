# Generated by Django 4.1.7 on 2023-03-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_date_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание датчика'),
        ),
    ]