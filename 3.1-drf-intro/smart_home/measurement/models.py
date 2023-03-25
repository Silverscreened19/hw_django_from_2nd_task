
from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название датчика')
    description = models.CharField(
        max_length=300, verbose_name='Описание датчика')

    def __str__(self):
        return self.name



class Measurement(models.Model):
    id_sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='ID датчика')
    temperature = models.FloatField(verbose_name='Температура')
    date_measure = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    image = models.ImageField(null=True, verbose_name='Изображение с датчика')
