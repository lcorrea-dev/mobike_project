from django.urls import path
from rest_framework import routers
from .views import BicyclesViewSet

router = routers.DefaultRouter()
router.register('bicycles', BicyclesViewSet)

urlpatterns = router.urls
