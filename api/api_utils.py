import pandas as pd
import json

def consumo_last_7d(user_id: int) -> list:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list
    """
    df = pd.read_csv(f'./consumo_user_{user_id}.csv')

    df = df[df['datetime'].between('2013-02-01', '2013-02-07 23:30')].copy()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['dia'] = df['datetime'].apply(lambda x: x.day)

    data = df.groupby('dia').aggregate({'datetime': 'first','total': 'sum'})
    # data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%d-%m-%y'))
    data['datetime'] = data['datetime'].apply(lambda x: x.strftime('%A'))

    response = json.loads(data.to_json())

    # Arreglando datos
    new_response = []
    for i in range(1, 8):
        value = {
            'day': response['datetime'][f'{i}'],
            'value': response['total'][f'{i}']
        }
        new_response.append(value)

    return new_response

