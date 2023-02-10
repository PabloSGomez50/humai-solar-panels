import pandas as pd
import api_formato
from datetime import datetime, timedelta
# import json

CSV_CONSUMO = './consumo_user_{0}.csv'
CSV_PROD = './user_{0}.csv'

DAYS_DIFF = 2 + 365 * 10

def get_datetimes(days = 6, months = 0):
    """
    Funcion para obtener los registros de interes, de una semana o varios meses
    """
    
    max_day = datetime.today() - timedelta(days=DAYS_DIFF)

    if months == 0:
        min_day = max_day - timedelta(days=days)
    else:
        min_day = datetime(year=max_day.year, month=1, day=1)

    lim_min = min_day.strftime('%Y-%m-%d')
    lim_max = max_day.strftime('%Y-%m-%d') + ' 23:59'

    return (lim_min, lim_max)


def consumo_last_7d(user_id: int) -> list:
    """
    Accede al dataset y devuelve una lista con los datos de los ultimos 7 dias
    y el total de consumo

    Input: user_id -> int
    Output: response -> list[{'day', 'value'}]
    """
    
    df = pd.read_csv(CSV_CONSUMO.format(user_id))
    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Dia'] = df['Datetime'].dt.day

    df_ = df.groupby('Dia').aggregate({'Datetime': 'first','Total': 'sum'})
    df_['Datetime'] = df_['Datetime'].dt.strftime('%A')

    data = df_.to_records(index=False)
    
    total = round(sum(map(lambda x: x[1], data)), 2)
    response = [{'day': x[0], 'value': x[1]} for x in data]
    response.append({'day': 'Total', 'value': total})

    return response


def prod_last_7(user_id: int) -> dict:
    """
    Accede al dataset de producciony devuelve una lista 
    con los datos relevantes de los ultimos 7 dias
    
    Datos: Total diario | Promedio diario | Horas de mayor produccion

    Input: user_id -> int
    Output: response -> list[dict]
    """
    df = pd.read_csv(CSV_PROD.format(user_id), usecols=['Datetime', 'Produccion'])

    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Dia'] = df['Datetime'].dt.day
    df['Hora'] = df['Datetime'].dt.hour

    # Info 1
    df1 = df.groupby('Dia').aggregate({'Datetime': 'first', 'Produccion': 'mean'})
    df1['Datetime'] = df1['Datetime'].dt.strftime('%A')

    data1 = df1.to_records(index=False)
    
    data1 = [{'dia': x[0], 'promedio': round(x[1], 3)} for x in data1]

    # Info 2
    df2 = df.groupby('Hora').aggregate({'Produccion': 'sum'})
    df2 = df2[df2['Produccion'] > 0.1]

    data2 = df2.to_records()
    
    data2 = [{'hora': str(x[0]), 'total': round(x[1], 3)} for x in data2]
    
    return {'prom': data1,'horas': data2}


def prod_history(user_id: int, span: str) -> list:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list['day', 'value']
    """
    
    df = pd.read_csv(CSV_PROD.format(user_id), usecols=['Datetime', 'Produccion'])

    # df = df[df['Datetime'].between('2013-01-02', '2013-06-31 23:30')].copy()

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Dia'] = df['Datetime'].dt.day
    df['Mes'] = df['Datetime'].dt.month
    df['Anio'] = df['Datetime'].dt.year

    df_ = df.groupby(by=['Anio','Mes','Dia']).aggregate({'Datetime': 'first','Produccion': 'sum'})

    return api_formato.format_calendario(df_)

def prod_by_month() -> list:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """

    df = pd.read_csv(CSV_PROD.format(1), usecols=['Datetime', 'Produccion'])

    t_min, t_max = get_datetimes(months=1)

    # Filtrar un par de meses
    df1 = df[df['Datetime'].between(t_min, t_max)].copy()
    df1['Datetime'] = pd.to_datetime(df1['Datetime'])

    # Agrupar por mes y dia
    df1['Dia'] = df1['Datetime'].dt.day
    df1['Mes'] = df1['Datetime'].dt.month
    df1 = df1.groupby(by=['Mes','Dia']).aggregate({'Datetime': 'first','Produccion': 'sum'})

    # Set indices finales
    df1.reset_index(drop=True, inplace=True)

    # Filtrar los datos
    response = api_formato.format_linea(df1)

    return response