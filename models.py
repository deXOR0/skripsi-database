from django.db import models
import uuid


class Timestamp(models.Model):
    time_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'timestamps'
        app_label = ''


class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'cities'
        app_label = ''


class District(models.Model):
    district_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'districts'
        app_label = ''


class Pollutant(models.Model):
    pollutant_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.ForeignKey(Timestamp, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    NO2 = models.FloatField()
    CO = models.FloatField()
    O3 = models.FloatField()
    SO2 = models.FloatField()
    PM10 = models.FloatField()
    PM25 = models.FloatField()

    class Meta:
        db_table = 'pollutants'
        app_label = ''
