from rest_framework.serializers import ModelSerializer

from .models import Bicycle, ParkingLot


class BicycleSerializer(ModelSerializer):
    class Meta:
        model = Bicycle
        fields = ['id', 'purchase_date', 'qr_code',
                  'brand', 'model', 'm_traveled', 'is_locked', 'parking_lot']


class ParkingLotSerializer(ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = ['id', 'description', 'max_capacity',
                  'address', 'latitude', 'longitude', 'bicycles']
