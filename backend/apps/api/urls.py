from django.urls import path
from rest_framework import routers
from .views import BicyclesViewSet, ParkingLotsViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('bicycles', BicyclesViewSet)
router.register('parkinglots', ParkingLotsViewSet)


urlpatterns = router.urls
urlpatterns += path('login', obtain_auth_token),
