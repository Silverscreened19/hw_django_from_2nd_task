from django.urls import path
from measurement.views import CreateMeasurement, SensorView, SensorsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
