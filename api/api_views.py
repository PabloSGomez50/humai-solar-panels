import pandas as pd
import api_formato
from datetime import datetime, timedelta

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

def get_prod(user_id: int) -> pd.DataFrame:
    """
    Obtener el dataframe a partir del csv del usuario

    Input:
        - user_id: int
    Output:
        - Dataframe con fecha parseada ['index', 'Datetime', 'Produccion']

    """
    columns = ['Datetime', 'Produccion']

    return pd.read_csv(CSV_PROD.format(user_id), usecols=columns, parse_dates=['Datetime'])


def get_consumo(user_id: int) -> pd.DataFrame:
    
    return pd.read_csv(CSV_CONSUMO.format(user_id), parse_dates=['Datetime'])


def consumo_last_7d(user_id: int) -> list:
    """
    Accede al dataset y devuelve una lista con los datos de los ultimos 7 dias
    y el total de consumo

    Input: user_id -> int
    Output: response -> list[{'day', 'value'}]
    """
    
    df = get_consumo(user_id)
    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)]
    df['Dia'] = df['Datetime'].dt.day

    df_ = df.groupby('Dia').aggregate({'Datetime': 'first','Total': 'sum'})
    df_['Datetime'] = df_['Datetime'].dt.strftime('%A')

    # data = df_.to_records(index=False)
    
    # total = round(sum(map(lambda x: x[1], data)), 2)
    
    # response = [{
    #     'day': x[0], 
    #     'value': round(x[1], 2)
    #     } 
    #     for x in data ]

    # response.append({'day': 'Total', 'value': total})

    return df_


def prod_last_7(user_id: int) -> dict:
    """
    Accede al dataset de producciony devuelve una lista 
    con los datos relevantes de los ultimos 7 dias
    
    Datos: Total diario | Promedio diario | Horas de mayor produccion

    Input: user_id -> int
    Output: response -> list[dict]
    """
    df = get_prod(user_id)

    t_min, t_max = get_datetimes()
    df = df[df['Datetime'].between(t_min, t_max)]
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


def prod_calendar(user_id: int) -> list:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list['day', 'value']
    """
    
    df = get_prod(user_id)

    df1 = df.resample('1D', on='Datetime').sum()
    df1['Fecha'] = df1.index.strftime('%Y-%m-%d')
    
    return df1

def prod_by_month(user_id: int) -> list:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """

    df = get_prod(user_id)

    t_min, t_max = get_datetimes(months=1)

    # print(t_min, t_max)

    # Filtrar un par de meses
    df = df[df['Datetime'].between(t_min, t_max)]

    # Dimensionar l
    df1 = df.resample('1D', on='Datetime').sum()

    # # Filtrar los datos
    # response = api_formato.format_linea(df)

    return df1


def prod_history(user_id: int) -> list:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """

    df = get_prod(user_id)

    t_min, t_max = get_datetimes(months=1)

    # Filtrar un par de meses
    df = df[df['Datetime'].between(t_min, t_max)]

    df = df.resample('1D', on='Datetime').sum()
    # # Agrupar por mes y dia
    # df['Dia'] = df['Datetime'].dt.day
    # df['Mes'] = df['Datetime'].dt.month
    # df = df.groupby(by=['Mes','Dia']).aggregate({'Datetime': 'first','Produccion': 'sum'})

    # # Set indices finales
    # df.reset_index(drop=True, inplace=True)

    # Filtrar los datos
    # response = api_formato.format_linea(df)

    return df

def get_table(user_id: int) -> list:

    df_con = get_consumo(user_id)
    df_prod = get_prod(user_id)

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
