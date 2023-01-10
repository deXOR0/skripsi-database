from db import connect_to_db
import json
import datetime
import os
import shutil


def load_json_data():
    data = []
    with open('pollution_data.json') as f:
        data = json.loads(f.read())['data']

    return data


def load_json_data_multiple():
    data = []

    files = [f for f in os.listdir('data/') if f.endswith('.json')]
    files.sort()

    for _file in files:
        with open(os.path.join('data', _file)) as f:
            data.append(json.loads(f.read()))

        shutil.move(os.path.join('data/', _file),
                    os.path.join('uploaded/', _file))
    return data


def create_timestamp(_timestamp):
    timestamp = Timestamp(
        timestamp=datetime.datetime.fromtimestamp(_timestamp))
    timestamp.save()

    return timestamp


def get_district(district_name: str):
    return District.objects.filter(district_name=district_name)[0]


def create_pollutant(timestamp, district, pollutants):
    pollutant = Pollutant(
        timestamp=timestamp,
        district=district,
        no2=pollutants['NO2'],
        co=pollutants['CO'],
        o3=pollutants['O3'],
        so2=pollutants['SO2'],
        pm10=pollutants['PM10'],
        pm25=pollutants['PM25'],
    )

    pollutant.save()

    return pollutant


def insert_data_to_db(data):
    for d in data:

        timestamp = create_timestamp(d['timestamp'])

        locations = d['locations']

        districts = {}

        for city in locations:
            for district in locations[city]:
                if district not in districts:
                    districts[district] = get_district(district)

                pollutant = create_pollutant(
                    timestamp, districts[district], locations[city][district])

                print(pollutant)


if __name__ == '__main__':
    connect_to_db()
    from models import *

    data = load_json_data_multiple()

    insert_data_to_db(data)
