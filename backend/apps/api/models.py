from django.db import models
from django.conf import settings


class Bicycle(models.Model):
    purchase_date = models.DateField()
    qr_code = models.CharField(max_length=10)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    m_traveled = models.FloatField()
    is_locked = models.BooleanField()


class Cyclist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)


class BipMobike(models.Model):
    current_balance = models.IntegerField()
    expiration_date = models.DateField()
    is_active = models.BooleanField()


class ServiceFee(models.Model):
    charge = models.FloatField()
    time_in_minutes = models.IntegerField()
    starting_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)


class Route(models.Model):
    cyclist = models.ForeignKey(
        Cyclist, related_name='routes', on_delete=models.CASCADE)
    bicycle = models.ForeignKey(
        Bicycle, related_name='routes', on_delete=models.CASCADE)
    starting_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost = models.IntegerField()


class Rating(models.Model):
    route = models.OneToOneField(
        Route, related_name='rating', null=True, on_delete=models.CASCADE)
    service_rating = models.IntegerField()
    bicycle_rating = models.IntegerField()
    parking_lot_rating = models.IntegerField()
    general_comment = models.CharField(max_length=500)


class Coordinates(models.Model):
    route = models.ForeignKey(
        Route, related_name='coordinates', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
