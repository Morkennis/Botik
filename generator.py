from datetime import datetime, timedelta
from config import names
import json


def _main():
    def compute_ind(i):
        return (i + magic_number) % len(names)

    resdict = dict()
    magic_number = 8
    i2 = -1
    for i in range(0, 100):
        date = (datetime.now() + timedelta(days=i))

        if date.weekday() == 6 or date.weekday() == 1:
            continue

        i2 += 1
        date = date.strftime('%d.%m.%Y')

        resdict.update({date: names[compute_ind(i2)]})

    with open('data.json', 'w', encoding='utf-8') as fp:
        json.dump(resdict, fp)


_main()