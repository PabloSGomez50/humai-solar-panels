import pandas as pd
import api_formato
# import json

CSV_CONSUMO = './consumo_user_{0}.csv'
CSV_PROD = './user_{0}.csv'

def consumo_last_7d(user_id: int) -> list:
    """
    Accede al dataset y devuelve una lista con los datos de los ultimos 7 dias
    y el total de consumo

    Input: user_id -> int
    Output: response -> list[{'day', 'value'}]
    """
    df = pd.read_csv(CSV_CONSUMO.format(user_id))

    df = df[df['datetime'].between('2013-02-01', '2013-02-07 23:30')].copy()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['dia'] = df['datetime'].dt.day

    df_ = df.groupby('dia').aggregate({'datetime': 'first','total': 'sum'})
    # df_['datetime'] = df_['datetime'].apply(lambda x: x.strftime('%d-%m-%y'))
    df_['datetime'] = df_['datetime'].dt.strftime('%A')

    data = df_.to_records(index=False)
    
    total = round(sum(map(lambda x: x[1], data)), 2)
    response = [{'day': x[0], 'value': x[1]} for x in data]
    response.append({'day': 'Total', 'value': total})

    return response


def prod_history(span: str) -> list:
    """
    Accede al dataset y devuelvo un json con los datos de los ultimos 7 dias

    Input: user_id -> int
    Output: response -> list['day', 'value']
    """
    df = pd.read_csv(CSV_PROD.format(1), usecols=['Datetime', 'Produccion'])

    df = df[df['Datetime'].between('2013-01-02', '2013-06-31 23:30')].copy()

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Dia'] = df['Datetime'].dt.day
    df['Mes'] = df['Datetime'].dt.month

    df_ = df.groupby(by=['Mes','Dia']).aggregate({'Datetime': 'first','Produccion': 'sum'})
    df_['Datetime'] = df_['Datetime'].dt.strftime('%Y-%m-%d')

    data = df_.to_records(index=False)


    return [{'day': x[0], 'value': round(x[1], 2)} for x in data]

def prod_by_month() -> list:
    """
    Funcion para el grafico de lineas
    Busca clasificar la produccion de los ultimos tres meses por dia
    """

    df = pd.read_csv(CSV_PROD.format(1), usecols=['Datetime', 'Produccion'])

    # Filtrar un par de meses
    df1 = df[df['Datetime'].between('2013-01-01', '2013-03-31 23:30')].copy()
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