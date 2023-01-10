from django.db import models
import uuid


class Timestamp(models.Model):
    time_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'timestamps'
        app_label = ''

    def __repr__(self):
        return str({'time_id': self.time_id, 'timestamp': self.timestamp})

    def __str__(self):
        return str({'time_id': self.time_id, 'timestamp': self.timestamp})


class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'cities'
        app_label = ''

    def __repr__(self):
        return str({'city_id': self.city_id, 'city_name': self.city_name})


class District(models.Model):
    district_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'districts'
        app_label = ''

    def __repr__(self):
        return str({'district_id': self.district_id, 'city': self.city, 'district_name': self.district_name})


class Pollutant(models.Model):
    pollutant_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.ForeignKey(Timestamp, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    no2 = models.FloatField()
    co = models.FloatField()
    o3 = models.FloatField()
    so2 = models.FloatField()
    pm10 = models.FloatField()
    pm25 = models.FloatField()

    class Meta:
        db_table = 'pollutants'
        app_label = ''

    def __repr__(self):
        return str({
            'timestamp': self.timestamp,
            'district': self.district,
            'no2': self.no2,
            'co': self.co,
            'o3': self.o3,
            'so2': self.so2,
            'pm10': self.pm10,
            'pm25': self.pm25,
        })

    def __str__(self):
        return str({
            'timestamp': self.timestamp,
            'district': self.district,
            'no2': self.no2,
            'co': self.co,
            'o3': self.o3,
            'so2': self.so2,
            'pm10': self.pm10,
            'pm25': self.pm25,
        })
