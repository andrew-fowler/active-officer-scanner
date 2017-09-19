import json
import os


def file_exists(filepath):
    return os.path.isfile(filepath)


def file_is_older_than_an_hour(filepath):
    import datetime
    today = datetime.datetime.today()
    file_date = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
    duration = today - file_date
    return duration.seconds >= (60 * 60)


def get_json_from_file(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)
