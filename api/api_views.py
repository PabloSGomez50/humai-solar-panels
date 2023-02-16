import pandas as pd
from datetime import datetime, timedelta


DAYS_DIFF = 2 + 365 * 10

def get_datetimes(days = 6, months = 0, span: str = None):
    """
    Funcion para obtener los registros de interes, de una semana o varios meses
    """
    
    today = datetime.today() - timedelta(days=DAYS_DIFF)

    if span == '1D':
        days = 0
    elif span == '1M':
        days = 1


    if months == 0:
        min_day = today - timedelta(days=days)
    else:
        min_day = datetime(year=today.year, month=1, day=1)

    lim_min = min_day.strftime('%Y-%m-%d')
    lim_max = today.strftime('%Y-%m-%d') + ' 23:59'

    return (lim_min, lim_max)


def consumo_last_7d(df: pd.DataFrame) -> list:
    """
    Accede al dataset y devuelve una lista con los datos de los ultimos 7 dias
    y el total de consumo

    Input: user_id -> int
    Output: response -> list[{'day', 'value'}]
    """
    
    # df = get_consumo(user_id)
    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()
    df['Dia'] = df['Datetime'].dt.day

    df_ = df.groupby('Dia').aggregate({'Datetime': 'first','Total': 'sum'})
    df_['Datetime'] = df_['Datetime'].dt.dayofweek

    return df_


def consumo_now(df: pd.DataFrame) -> pd.DataFrame:
    """
    Accede al dataset y devuelve una lista con los datos de la ultima media hora

    Input: user_id -> int
    Output: response -> DataFrame
    """

    # df = get_consumo(user_id)
    # Trae el dia de 2012/2013
    now = datetime.now() - timedelta(days=DAYS_DIFF)
    delay = now - timedelta(minutes=55)

    lower = delay.strftime('%Y-%m-%d %H:%M')
    upper = now.strftime('%Y-%m-%d %H:%M')

    df = df[df['Datetime'].between(lower, upper)]
    df_ = df.tail(1)

    return df_


def prod_last_7(df: pd.DataFrame) -> dict:
    """
    Accede al dataset de producciony devuelve una lista 
    con los datos relevantes de los ultimos 7 dias
    
    Datos: Total diario | Promedio diario | Horas de mayor produccion

    Input: user_id -> int
    Output: response -> list[dict]
    """
    # df = get_prod(user_id)

    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()
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


def prod_calendar(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list['day', 'value']
    """
    
    # df = get_prod(user_id)

    # Seleccionar el año
    df = df[df['Datetime'].dt.year == year]

    # Separar por dia
    df1 = df.resample('1D', on='Datetime').sum()
    df1['Fecha'] = df1.index.strftime('%Y-%m-%d')
    
    return df1


def prod_history(df: pd.DataFrame, span: str) -> pd.DataFrame:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """

    # df = get_prod(user_id)
    print(span)

    t_min, t_max = get_datetimes(months=1)

    # Filtrar un par de meses
    df = df[df['Datetime'].between(t_min, t_max)]

    df = df.resample('1D', on='Datetime').sum()

    return df

def get_table(df_con: pd.DataFrame, df_prod:pd.DataFrame) -> pd.DataFrame:

    # df_con = get_consumo(user_id)
    # df_prod = get_prod(user_id)

    df_con = df_con.resample('1D', on='Datetime').sum()
    df_prod = df_prod.resample('1D', on='Datetime').sum()

    df_final = df_con.join(df_prod, how='inner')

    names = {
        # 'Datetime': 'Fecha',
        'GC': 'Consumo general',
        'CL': 'Consumo controlado',
        'Total': 'Consumo Total'
        }

    df_final = df_final.round(decimals=3)
    df_final['Fecha'] = df_final.index.strftime('%Y-%m-%d')
    df_final.reset_index(drop=True, inplace=True)
    df_final['id'] = df_final.index
    df_final.rename(columns=names,inplace=True)

    # data = df_final.to_dict(orient='records')

    return df_final

