from .models import Sensor
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.serializers import SensorSerializer, CreateMeasurementSerializer, SensorDetailSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurement(CreateAPIView):
    serializer_class = CreateMeasurementSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
