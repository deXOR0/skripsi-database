from db import connect_to_db
import json
import datetime


def load_json_data():
    data = []
    with open('pollution_data.json') as f:
        data = json.loads(f.read())['data']

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
        NO2=pollutants['NO2'],
        CO=pollutants['CO'],
        O3=pollutants['O3'],
        SO2=pollutants['SO2'],
        PM10=pollutants['PM10'],
        PM25=pollutants['PM25'],
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

    data = load_json_data()

    insert_data_to_db(data)
