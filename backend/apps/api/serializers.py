from rest_framework.serializers import ModelSerializer

from .models import Bicycle


class BicycleSerializer(ModelSerializer):
    class Meta:
        model = Bicycle
        fields = ['id', 'purchase_date', 'qr_code',
                  'brand', 'model', 'm_traveled', 'is_locked']
