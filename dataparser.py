import requests
from datetime import datetime


#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER
#TEMPORARILY OUT OF ORDER


class DateNotFoundException(Exception):
    pass


class DataParser:
    def __init__(self, API, link='https://sheetdb.io/api/v1/'):
        self.link = link
        self.API = API
        self.endpoint = f"{link}{API}"

        self._creation_date = datetime.now().timestamp()

        print(f"{int(self._creation_date)} Data parser object created")

    def get_name_by_date(self, date) -> str:

        for i in range(1, 9):

            res = requests.get(f"{self.endpoint}/search?{i}date={date}").json()

            if res != []:
                return res[0]['name']
            else:
                pass

    def get_columns_names(self):
        res = requests.get(f'{self.endpoint}/keys').text
        print(res)
