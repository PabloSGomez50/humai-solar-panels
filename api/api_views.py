import pandas as pd
from datetime import datetime, timedelta


DAYS_DIFF = 2 + 365 * 10

def get_datetimes(days = 6, months = 0, minutes = 0):
    """
    Funcion para obtener los registros de interes, de una semana o varios meses
    """
    
    today = datetime.today() - timedelta(days=DAYS_DIFF)

    if months != 0:
        mes = today.month + 1
        # dia = today.day
        anio = today.year
        
        if mes - months < 1:
            mes += 12
            anio -= 1 

        min_day = datetime(year=anio, month=mes - months, day=1)
    else:
        min_day = today - timedelta(days=days, minutes = minutes)


    lim_min = min_day.strftime('%Y-%m-%d')
    # lim_max = today.strftime('%Y-%m-%d') + ' 23:59'
    lim_max = today.strftime('%Y-%m-%d %H:%M')

    return (lim_min, lim_max)


def consumo_now(df: pd.DataFrame) -> pd.DataFrame:
    """
    Accede al dataset y devuelve una lista con los datos de la ultima media hora

    Input: user_id -> int
    Output: response -> DataFrame
    """
    # Trae el dia de 2012/2013
    # now = datetime.now() - timedelta(days=DAYS_DIFF)
    # delay = now - timedelta(minutes=55)

    # lower = delay.strftime('%Y-%m-%d %H:%M')
    # upper = now.strftime('%Y-%m-%d %H:%M')

    df = df[df['Datetime'].between(get_datetimes(minutes=55))]
    df_ = df.tail(1)

    return df_


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


def prod_last_7(df: pd.DataFrame) -> pd.DataFrame:
    """
    Accede al dataset de producciony devuelve una lista 
    con los datos relevantes de los ultimos 7 dias
    
    Datos: Total diario | Promedio diario | Horas de mayor produccion

    Input: user_id -> int
    Output: df -> 'Datetime' | 'total'
    """

    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()

    df1 = df.resample('1D', on='Datetime').sum()
    # total = round(df1['Produccion'].sum(), 3)
    df1.rename(columns={'Produccion': 'Total'}, inplace=True)
    df1['Datetime'] = df1.index.dayofweek.astype(int)
    
    return df1

def prod_month(df: pd.DataFrame) -> pd.DataFrame:

    df = df[df['Datetime'].between(*get_datetimes(months=7))].copy()

    df1 = df.resample('1M', on='Datetime').sum()

    df1.rename(columns={'Produccion': 'Total'}, inplace=True)
    df1['Datetime'] = df1.index.month

    return df1


def consumo_month(df: pd.DataFrame) -> pd.DataFrame:

    df = df[df['Datetime'].between(*get_datetimes(months=7))].copy()

    df1 = df.resample('1M', on='Datetime').sum()

    # df1.rename(columns={'Produccion': 'Total'}, inplace=True)
    df1['Datetime'] = df1.index.month

    return df1


def horas(df: pd.DataFrame) -> list:

    # Preparar el dataframe
    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)].copy()
    df['hora'] = df['Datetime'].dt.hour

    # Hacer groupby y armar las columnas
    df2 = df.groupby('hora').aggregate({'Produccion': 'sum'})
    df2 = df2[df2['Produccion'] > 0.1]
    df2.reset_index(inplace=True)

    df2.rename(columns={'Produccion': 'total'}, inplace=True)
    df2['total'] = round(df2['total'], 3)
    
    return df2


def prod_calendar(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list['day', 'value']
    """
    # Seleccionar el año
    df = df[df['Datetime'].dt.year == year]

    # Separar por dia
    df1 = df.resample('1D', on='Datetime').sum()
    df1['Fecha'] = df1.index.strftime('%Y-%m-%d')
    
    return df1


def prod_history(df: pd.DataFrame, span: str, sample: str) -> pd.DataFrame:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """
    if span == '1Y':
        days = 0
        months = 12
    elif span == '3M':
        days = 0
        months = 3
    elif span == '1M':
        days = 0
        months = 1
    elif span == '1W':
        days = 6
        months = 0
    else: 
        days = 0
        months = 0

    t_min, t_max = get_datetimes(days=days, months=months)
    
    # Filtrar un par de meses
    df = df[df['Datetime'].between(t_min, t_max)]

    df = df.resample(sample, on='Datetime').sum()

    return df


def get_table(df_con: pd.DataFrame, df_prod:pd.DataFrame) -> pd.DataFrame:

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

    return df_final
