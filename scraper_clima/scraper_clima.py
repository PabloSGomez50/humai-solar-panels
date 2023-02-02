import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import demjson
from unicodedata import normalize
from datetime import datetime, timedelta
import re


def get_data(date, month, year):
    cookies = {
        '_pbjs_userid_consent_data': '3524755945110770',
        '_sharedID': 'c673f09b-e619-43c6-971b-c0d67e16f49c',
        '__gads': 'ID=29480aa4712e38d7:T=1675200257:S=ALNI_MZv1zk4XHCqgmGiU-c0XTo4bbdBww',
        '__qca': 'P0-443300669-1675200254756',
        'TAPAD': '%7B%22id%22%3A%228013ff31-f61b-4c8f-981e-dfe29af1fd4f%22%7D',
        'uids': 'eyJ0ZW1wVUlEcyI6eyJhbXgiOnsidWlkIjoiZjU0N2ZlOGQtYWMwZS00ODZhLThlNGMtOWRmNDUwNWVhZmZiIiwiZXhwaXJlcyI6IjIwMjMtMDItMTRUMjE6MjQ6MTcuMzYwODY0NDA4WiJ9LCJvbmV0YWciOnsidWlkIjoiRkJIR2FnZkloWnU0V1R0blljajVOTk82bjhyeFhrTHZUb0s3T29vQUhfUSIsImV4cGlyZXMiOiIyMDIzLTAyLTE0VDIxOjI0OjIwLjEzMzg1NTQ2OFoifSwib3BlbngiOnsidWlkIjoiOGJiM2NmNDktYjc4YS0wNGMwLTBkY2ItYzdlMWJkYTQyMzNhIiwiZXhwaXJlcyI6IjIwMjMtMDItMTRUMjE6Mzc6NTUuOTg1ODc2NTg1WiJ9LCJzb3ZybiI6eyJ1aWQiOiJFckpoVkxaSGdRbllKd3REVFVhRDFIaWUiLCJleHBpcmVzIjoiMjAyMy0wMi0xNVQwMjoxNjozMi41MzMzMzEwNjJaIn19LCJiZGF5IjoiMjAyMy0wMS0zMVQyMToyNDoxNy4zNjA4NTYyMjlaIn0=',
        'TADANON': 'cEVzaHJDOUlqcHpRZXNKMFZHWEpKRUtuanlVR3BnTkdldmlIWTFNcmlYSFhXM0ZkdWJRczA5ZEJDa0syeVJKRA--',
        '__gpi': 'UID=000009ea849cce83:T=1675200257:RT=1675305526:S=ALNI_MaujIx1XiDV-pqu1-3wyBjN3tHc6g',
        'cto_bundle': 'k5zU0l9sYkFNUTg4SkdrT2Q4VXNYNVZyR2dHVXFFdUZvVEx4JTJGQ0dJRFY1cm9yak5JM2R6YVYzS3pVRjFtUnFJTGNpbjJRZVNzS3lRSU82VmNSMG9xUXgwbDlXNUQySWQlMkZiU1BXT1A3JTJGcW54T20lMkJKMXBXJTJCOWVCeXN1UmNNTHhHSDRkNU9VOXdDQ2piU2poUjBIWnczU04yMHZ3JTNEJTNE',
        'cto_bidid': 'yZo5QV92Z3RleHd4NHQ5bUFMdDJrY3lEcVQ1T0Z5T3diQVglMkJkYlNFdG0xc3JIRGRwZ0ZrM0lqcVVCcVJpQlJxSWFtcXBRaWhpVE85b1NSUlUlMkJoZjglMkZGWE51Z0twdEVaUXNRTmEya3A3NDhMUmQlMkJ1eVlXMEFMRU1zZ2FzNXVvVHpRVWlm',
    }

    headers = {
        'authority': 'www.timeanddate.com',
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        # 'cookie': '_pbjs_userid_consent_data=3524755945110770; _sharedID=c673f09b-e619-43c6-971b-c0d67e16f49c; __gads=ID=29480aa4712e38d7:T=1675200257:S=ALNI_MZv1zk4XHCqgmGiU-c0XTo4bbdBww; __qca=P0-443300669-1675200254756; TAPAD=%7B%22id%22%3A%228013ff31-f61b-4c8f-981e-dfe29af1fd4f%22%7D; uids=eyJ0ZW1wVUlEcyI6eyJhbXgiOnsidWlkIjoiZjU0N2ZlOGQtYWMwZS00ODZhLThlNGMtOWRmNDUwNWVhZmZiIiwiZXhwaXJlcyI6IjIwMjMtMDItMTRUMjE6MjQ6MTcuMzYwODY0NDA4WiJ9LCJvbmV0YWciOnsidWlkIjoiRkJIR2FnZkloWnU0V1R0blljajVOTk82bjhyeFhrTHZUb0s3T29vQUhfUSIsImV4cGlyZXMiOiIyMDIzLTAyLTE0VDIxOjI0OjIwLjEzMzg1NTQ2OFoifSwib3BlbngiOnsidWlkIjoiOGJiM2NmNDktYjc4YS0wNGMwLTBkY2ItYzdlMWJkYTQyMzNhIiwiZXhwaXJlcyI6IjIwMjMtMDItMTRUMjE6Mzc6NTUuOTg1ODc2NTg1WiJ9LCJzb3ZybiI6eyJ1aWQiOiJFckpoVkxaSGdRbllKd3REVFVhRDFIaWUiLCJleHBpcmVzIjoiMjAyMy0wMi0xNVQwMjoxNjozMi41MzMzMzEwNjJaIn19LCJiZGF5IjoiMjAyMy0wMS0zMVQyMToyNDoxNy4zNjA4NTYyMjlaIn0=; TADANON=cEVzaHJDOUlqcHpRZXNKMFZHWEpKRUtuanlVR3BnTkdldmlIWTFNcmlYSFhXM0ZkdWJRczA5ZEJDa0syeVJKRA--; __gpi=UID=000009ea849cce83:T=1675200257:RT=1675305526:S=ALNI_MaujIx1XiDV-pqu1-3wyBjN3tHc6g; cto_bundle=k5zU0l9sYkFNUTg4SkdrT2Q4VXNYNVZyR2dHVXFFdUZvVEx4JTJGQ0dJRFY1cm9yak5JM2R6YVYzS3pVRjFtUnFJTGNpbjJRZVNzS3lRSU82VmNSMG9xUXgwbDlXNUQySWQlMkZiU1BXT1A3JTJGcW54T20lMkJKMXBXJTJCOWVCeXN1UmNNTHhHSDRkNU9VOXdDQ2piU2poUjBIWnczU04yMHZ3JTNEJTNE; cto_bidid=yZo5QV92Z3RleHd4NHQ5bUFMdDJrY3lEcVQ1T0Z5T3diQVglMkJkYlNFdG0xc3JIRGRwZ0ZrM0lqcVVCcVJpQlJxSWFtcXBRaWhpVE85b1NSUlUlMkJoZjglMkZGWE51Z0twdEVaUXNRTmEya3A3NDhMUmQlMkJ1eVlXMEFMRU1zZ2FzNXVvVHpRVWlm',
        'referer': f'https://www.timeanddate.com/weather/australia/sydney/historic?month={month}&year={year}',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }


    response = requests.get(
        f'https://www.timeanddate.com/scripts/cityajax.php?n=australia/sydney&mode=historic&hd={date}&month={month}&year={year}&json=1',
        cookies=cookies,
        headers=headers,
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    return demjson.decode(soup.text)

def main():

    ls_datos_clima = []
    date_from = datetime(year=2012, month=7, day=1)
    date_to = datetime(year=2013, month=6, day=30)
    date_to = datetime(year=2012, month=7, day=1)
    date_iterador = date_from
    #regular_expresion_hora = '^(\d){1,2}:(\d){2} (am|pm)'
    regular_expresion_hora = '^(\d){1,2}:(\d){2}'

    while(date_iterador <= date_to):
        print (date_iterador, date_to)
        day = str(date_iterador.day)
        year = str(date_iterador.year)
        month = str(date_iterador.month)
        date = str(year) + ('00' + month)[-2:] + ('00' + day)[-2:]

        json_data = get_data(date, month, year)

        for index in range(len(json_data)):
            date = date_iterador.strftime('%Y-%m-%d')
            hour_am_pm = re.search(regular_expresion_hora, json_data[index]['c'][0]['h']).group()
            #hour_24 = datetime.strftime(datetime.strptime(hour_am_pm, "%I:%M %p"), "%H:%M")
            hour_24 = hour_am_pm
            temp = normalize('NFKD', json_data[index]['c'][2]['h'])
            weather = json_data[index]['c'][3]['h']
            wind = json_data[index]['c'][4]['h']
            humidity = json_data[index]['c'][6]['h'],
            barometer = json_data[index]['c'][7]['h'],
            visibility = normalize('NFKD', json_data[index]['c'][8]['h'])

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

        date_iterador = (date_iterador + timedelta(days=1))


    df_clima = pd.DataFrame.from_records(ls_datos_clima)
    df_clima.to_csv('./scraper_clima/clima_sidney.csv')  



if __name__ == '__main__':
    main()