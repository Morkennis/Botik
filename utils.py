import datetime
from datetime import datetime, timedelta
import json


def get_current_date():
    date = datetime.now().strftime("%d.%m.%Y")
    return date


def get_next_date():
    date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
    return date


def get_name(date: str) -> str:
    json_file = open('data.json')
    json_str = json_file.read()
    print(json_str)
    json_data = json.loads(json_str)
    return json_data[date]