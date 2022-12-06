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
    NO2 = models.FloatField()
    CO = models.FloatField()
    O3 = models.FloatField()
    SO2 = models.FloatField()
    PM10 = models.FloatField()
    PM25 = models.FloatField()

    class Meta:
        db_table = 'pollutants'
        app_label = ''

    def __repr__(self):
        return str({
            'timestamp': self.timestamp,
            'district': self.district,
            'NO2': self.NO2,
            'CO': self.CO,
            'O3': self.O3,
            'SO2': self.SO2,
            'PM10': self.PM10,
            'PM25': self.PM25,
        })

    def __str__(self):
        return str({
            'timestamp': self.timestamp,
            'district': self.district,
            'NO2': self.NO2,
            'CO': self.CO,
            'O3': self.O3,
            'SO2': self.SO2,
            'PM10': self.PM10,
            'PM25': self.PM25,
        })
