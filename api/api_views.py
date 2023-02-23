import pandas as pd
from api_utils import get_datetimes, get_time_predict, get_time_future_predict
from predicciones import hacer_predicciones

CANT_PREDICCIONES = 24


def data_now(df: pd.DataFrame) -> pd.DataFrame:
    """
    Accede al dataset y devuelve una lista con los datos de la ultima media hora

    Input: user_id -> int
    Output: response -> DataFrame
    """

    df = df[df['Datetime'].between(*get_datetimes(minutes=55))]
    # df_ = df.tail(1)

    return df.tail(1).copy()



def consumo_last_7d(df: pd.DataFrame) -> list:
    """
    Accede al dataset y devuelve una lista con los datos de los ultimos 7 dias
    y el total de consumo

    Input: user_id -> int
    Output: response -> list[{'day', 'value'}]
    """
    
    # df = get_consumo(user_id)
    # t_min, t_max = get_datetimes(days=6)
    df = df[df['Datetime'].between(* get_datetimes(days=6))].copy()
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
    
    df = df[df['Datetime'].between(*get_datetimes(days=6))].copy()

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
    df = df[df['Datetime'].between(*get_datetimes(days=6))].copy()
    df['hora'] = df['Datetime'].dt.hour

    # Hacer groupby y armar las columnas
    df2 = df.groupby('hora').aggregate({'Produccion': 'mean'})
    df2 = df2[df2['Produccion'] > 0.01]
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
    hours = 0
    months = 0
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
    elif span == '2D':
        days = 2
    else: 
        days = 0
        hours = 24

    # t_min, t_max = get_datetimes(days=days, months=months)
    
    # Filtrar un par de meses
    df = df[df['Datetime'].between(*get_datetimes(months=months, days=days, hours=hours))]

    df = df.resample(sample, on='Datetime').sum()
    # print(df)

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

    df_final['Diferencia'] = df_final['Produccion'] - df_final['Total']
    df_final = df_final.round(decimals=3)
    df_final['Fecha'] = df_final.index.strftime('%Y-%m-%d')
    df_final.reset_index(drop=True, inplace=True)
    df_final['id'] = df_final.index
    print(df_final.head())
    # df_final.rename(columns=names,inplace=True)
    # print(df_final.head())


    return df_final


def get_prediccion(df):
    """
    Funcion para limpiar el dataframe de la prediccion
    """

    
    df = df[df['Datetime'].between(*get_time_predict())]
    df = df.resample('1H', on='Datetime').sum()

    df = df.round(decimals=3)
    times = get_time_future_predict()
    # print(get_time_predict())
    # print(len(times), times)

    predicciones = pd.Series(hacer_predicciones(df['Produccion'], CANT_PREDICCIONES))
    # data = {'Produccion': predicciones}

    df_test = pd.DataFrame({'Produccion': predicciones})
    df_test['Datetime'] = pd.to_datetime(times)
    df_test.set_index('Datetime', inplace=True)
    # print(df_test)

    return df_test