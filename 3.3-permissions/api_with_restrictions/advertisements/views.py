from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.filters import OrderingFilter
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # permission_classes = [IsAuthenticated, IsOwner]
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ['creator', 'status', 'created_at']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    ordering_fields = ['id']

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        return []
