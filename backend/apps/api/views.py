from .models import Bicycle, ParkingLot

from rest_framework.viewsets import ModelViewSet
from .serializers import BicycleSerializer, ParkingLotSerializer
# To work with JSON data


class BicyclesViewSet(ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer

    def get_queryset(self):
        queryset = Bicycle.objects.all()
        purchase_date = self.request.query_params.get('purchase_date', None)
        qr_code = self.request.query_params.get('qr_code', None)
        brand = self.request.query_params.get('brand', None)
        model = self.request.query_params.get('model', None)
        m_traveled = self.request.query_params.get('m_traveled', None)
        is_locked = self.request.query_params.get('is_locked', None)
        if purchase_date is not None:
            queryset = queryset.filter(purchase_date=purchase_date)
        if qr_code is not None:
            queryset = queryset.filter(qr_code=qr_code)
        if brand is not None:
            queryset = queryset.filter(brand__icontains=brand)
        if model is not None:
            queryset = queryset.filter(model__icontains=model)
        if m_traveled is not None:
            queryset = queryset.filter(m_traveled__gte=m_traveled)
        if is_locked is not None:
            is_locked = is_locked.replace(
                'false', 'False').replace('true', 'True')
            queryset = queryset.filter(is_locked=is_locked)
        return queryset


class ParkingLotsViewSet(ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    def get_queryset(self):
        queryset = ParkingLot.objects.all()
        # purchase_date = self.request.query_params.get('purchase_date', None)
        # qr_code = self.request.query_params.get('qr_code', None)
        # brand = self.request.query_params.get('brand', None)
        # model = self.request.query_params.get('model', None)
        # m_traveled = self.request.query_params.get('m_traveled', None)
        # is_locked = self.request.query_params.get('is_locked', None)
        # if purchase_date is not None:
        #     queryset = queryset.filter(purchase_date=purchase_date)
        # if qr_code is not None:
        #     queryset = queryset.filter(qr_code=qr_code)
        # if brand is not None:
        #     queryset = queryset.filter(brand__icontains=brand)
        # if model is not None:
        #     queryset = queryset.filter(model__icontains=model)
        # if m_traveled is not None:
        #     queryset = queryset.filter(m_traveled__gte=m_traveled)
        # if is_locked is not None:
        #     is_locked = is_locked.replace(
        #         'false', 'False').replace('true', 'True')
        #     queryset = queryset.filter(is_locked=is_locked)
        return queryset
