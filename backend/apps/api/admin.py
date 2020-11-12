from django.contrib import admin
from .models import Bicycle, Cyclist, BipMobike, ServiceFee, Route, Rating, Coordinates

admin.site.register(Bicycle)
admin.site.register(Cyclist)
admin.site.register(BipMobike)
admin.site.register(ServiceFee)
admin.site.register(Route)
admin.site.register(Rating)
admin.site.register(Coordinates)
