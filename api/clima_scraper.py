import requests
from bs4 import BeautifulSoup
import pandas as pd
import demjson
from unicodedata import normalize
from datetime import datetime, timedelta
import re


FROM_DEFAULT = datetime(year=2012, month=7, day=1)
TO_DEFAULT = datetime(year=2012, month=7, day=5)


def get_data(date):
    """
    Realizar el request y parsear el texto en json

    input: DateTime
    output: Dict (Json format)
    """

    complete = datetime.strftime(date, "%Y%m%d")

    response = requests.get(
        f'https://www.timeanddate.com/scripts/cityajax.php?n=australia/sydney&mode=historic&hd={complete}&month={date.month}&year={date.year}&json=1'
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    return demjson.decode(soup.text)


def get_clima(date_from = FROM_DEFAULT, date_to = TO_DEFAULT) -> pd.DataFrame:
    """
    Obtener datos del clima entre dos fechas y guardarlos en archivo CSV

    Variables:
        - data_from: fecha de inicio de solicitud (DateTime)
        - date_to: fecha del final de solicitud (DateTime)
    """

    ls_datos_clima = []
    regular_expresion_hora = '^(\d){1,2}:(\d){2}'

    while(date_from <= date_to):
        print(date_from, date_to)

        json_data = get_data(date_from)

        for fila in json_data:

            fila = fila['c']

            date = date_from.strftime('%Y-%m-%d')
            #hour_24 = datetime.strftime(datetime.strptime(hour_am_pm, "%I:%M %p"), "%H:%M")
            hour_am_pm = re.search(regular_expresion_hora, fila[0]['h']).group()
            hour_24 = hour_am_pm
            temp = normalize('NFKD', fila[2]['h'])
            weather = fila[3]['h']
            wind = fila[4]['h']
            humidity = fila[6]['h'],
            barometer = fila[7]['h'],
            visibility = normalize('NFKD', fila[8]['h'])

            json_record = {
                'Date': date,
                'Hour': hour_24,
                'Temp': temp,
                'Weather': weather,
                'Wind': wind,
                'Humidity': humidity,
                'Barometer': barometer,
                'Visibility': visibility
            }

            ls_datos_clima.append(json_record)

        date_from = (date_from + timedelta(days=1))


    return pd.DataFrame.from_records(ls_datos_clima)



if __name__ == '__main__':
    print(get_clima())