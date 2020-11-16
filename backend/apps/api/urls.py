from django.urls import path
from rest_framework import routers
from .views import BicyclesViewSet, ParkingLotsViewSet

router = routers.DefaultRouter()
router.register('bicycles', BicyclesViewSet)
router.register('parkinglots', ParkingLotsViewSet)

urlpatterns = router.urls
