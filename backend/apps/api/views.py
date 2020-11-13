from .models import Bicycle

from rest_framework.viewsets import ModelViewSet
from .serializers import BicycleSerializer


class BicyclesViewSet(ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
