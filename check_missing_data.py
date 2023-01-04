from db import connect_to_db
import json
import datetime
import os
import shutil


def round_time(dt=None, roundTo=60):
    """Round a datetime object to any time lapse in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """
    if dt == None:
        dt = datetime.datetime.now()
    seconds = (dt.replace(tzinfo=None) - dt.min).seconds
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)


def get_timestamps():
    timestamps = Timestamp.objects.all().order_by('timestamp')
    return [x.timestamp for x in list(timestamps)]


def generate_timestamps(start):
    start = start.replace(hour=0, minute=0, second=0)
    print(f"{start=}")
    timestamps = []

    now = round_time(datetime.datetime.now(), roundTo=60*60)
    print(f"{now=}")

    for day in range(0, (now-start).days+1):
        new_day = start + datetime.timedelta(days=day)
        for hour in range(0, 23):
            new_timestamp = start + datetime.timedelta(days=day, hours=hour)
            if (new_timestamp.date() == new_day.date() and new_timestamp <= now):
                timestamps.append(new_timestamp)
            else:
                break

    return timestamps


if __name__ == '__main__':
    connect_to_db()
    from models import *

    db_timestamps = get_timestamps()

    timestamps = generate_timestamps(db_timestamps[0])

    missing = []

    for timestamp in timestamps:
        if timestamp not in db_timestamps:
            missing.append({
                "timestamp": timestamp,
                "utc": timestamp - datetime.timedelta(hours=7)
            })

    print(f'{len(missing)} timestamp(s) appeared to be missing')
    print(f'{len(db_timestamps)} timestamp(s) in database')
    print(f'{len(timestamps)} timestamp(s) should exists')

    with open('missing.json', 'w') as f:
        f.write(json.dumps(missing, default=str))
