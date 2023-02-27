from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import os 
from datetime import datetime, timedelta

from api_utils import get_index_group
from predicciones import hacer_predicciones
from scritps.limpiar_consumo import get_df_consumo
from scritps.limpiar_prod import get_prod_customer

import api_views
import api_formato
import clima_scraper
import clima_limpiar

CSV_CONSUMO = './data/consumo/consumo_user_{0}.csv'
CSV_PROD = './data/produccion/user_{0}.csv'
CSV_CLIMA = './data/clima_{0}_{1}.csv'
DAYS_DIFF = 2 + 365 * 10
CUSTOMER_ID = 1

CANT_PREDICCIONES = 24

app = FastAPI()

origins = [
    'http://127.0.0.1:5173',
    'https://humai-solar-panels.vercel.app',
    'https://frontend-humai-solar.vercel.app'
    
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


def get_prod(user_id: int) -> pd.DataFrame:
    """
    Obtener el dataframe a partir del csv del usuario
        Input: user_id: int
        Output: Dataframe con fecha parseada ['index', 'Datetime', 'Produccion']
    """
    columns = ['Datetime', 'Produccion']

    return pd.read_csv(CSV_PROD.format(user_id), usecols=columns, parse_dates=['Datetime'])


def get_consumo(user_id: int) -> pd.DataFrame:
    
    return pd.read_csv(CSV_CONSUMO.format(user_id), parse_dates=['Datetime'])


@app.on_event('startup')
def start_app():

    print('Es re flashero que pueda ejecutar funciontes de esta manera')

    today = datetime.today() - timedelta(days=DAYS_DIFF)
    
    if not os.path.exists(CSV_CLIMA.format(today.month, today.day)):
        today = datetime(year=today.year, month=today.month, day=today.day)

        to_date = today + timedelta(days=3)

        df = clima_scraper.get_clima(today, to_date)
        df_clean = clima_limpiar.clean_df(df)
        
        df_test = df_clean[df_clean.index.hour == 12].copy()

        df_test = df_test.loc[::2,:]

        df_test.drop(columns=['Visibility'], inplace=True)
        df_test.to_csv(CSV_CLIMA.format(today.month, today.day))


@app.get('/')
def root():

    return {'message': 'Hello World'}


@app.get('/select_user/{user_id}')
def select_user(user_id: int):
    """
    Opcion para seleccionar un usuario desde la 
    """
    if not os.path.exists(CSV_CONSUMO.format(user_id)):
        print('Se va a crear el archivo de consumo')
        df_con = get_df_consumo(user_id)
        df_con.to_csv(CSV_CONSUMO.format(user_id))
    
    if not os.path.exists(CSV_PROD.format(user_id)):
        print('Se va a crear el archivo de produccion')
        df_prod = get_prod_customer(user_id)
        df_prod.to_csv(CSV_PROD.format(user_id))
    
    return user_id


@app.get('/consumo')
def consumo_last_7d(user_id: int=CUSTOMER_ID):

    df = get_consumo(user_id)
    df_response = api_views.consumo_last_7d(df)
    response = api_formato.format_summary(df_response)

    return response


@app.get('/prod')
def resumen(user_id: int=CUSTOMER_ID):

    df = get_prod(user_id)
    df_response = api_views.prod_last_7(df)
    response = api_formato.format_summary(df_response)
    
    return response


@app.get('/clima')
def show_clima():

    today = datetime.today()
    df_clima = pd.read_csv(CSV_CLIMA.format(today.month, today.day), parse_dates=['Datetime'])

    df_clima.sort_index(inplace=True)

    response = api_formato.format_clima(df_clima)
    
    return response


@app.get('/summary')
def summary(user_id: int=CUSTOMER_ID):

    df_con = get_consumo(user_id)
    df_prod = get_prod(user_id)

    consumo_7d = api_views.consumo_last_7d(df_con)
    prod_7d = api_views.prod_last_7(df_prod)
    prod_mes = api_views.prod_month(df_prod)
    consumo_mes = api_views.consumo_month(df_con)
    
    return {
        'consumo_dia': api_formato.format_summary(consumo_7d),
        'prod_dia': api_formato.format_summary(prod_7d),
        'consumo_week': api_formato.format_summary(consumo_mes, week=False),
        'prod_week': api_formato.format_summary(prod_mes, week=False)
    }


@app.get('/hours')
def horas(user_id: int=CUSTOMER_ID):
    df = get_prod(user_id)
    df_response = api_views.horas(df)
    response = df_response.to_dict(orient='records')
    # response = api_formato.format_summary(df_response)

    return response
    

@app.get('/calendar/{year}')
def calendario(year: int, user_id: int=CUSTOMER_ID):

    df = get_prod(user_id)
    df_response = api_views.prod_calendar(df, year)
    response = api_formato.format_calendario(df_response)

    return response


@app.get('/line/{tipo}/{span}/{sample}')
def historia_telegram(tipo: bool, span: str='1M', sample: str='1D', user_id: int=CUSTOMER_ID):

    if tipo:
        df = get_prod(user_id)
    else:
        df = get_consumo(user_id)
    df_response = api_views.prod_history(df, span=span, sample=sample)

    index, group = get_index_group(sample, True)

    return api_formato.format_linea_telegram(df_response, index, tipo=tipo)


@app.get('/hist/{tipo}/{span}/{sample}')
def historia(tipo: bool, span: str='1M', sample: str='1D', user_id: int=CUSTOMER_ID):
    df1 = get_prod(user_id)
    df2 = get_consumo(user_id)

    # df2.drop(columns=['GC', 'CL'], inplace=True)

    df = pd.merge(df1, df2, left_on='Datetime', right_on='Datetime')

    df_response = api_views.prod_history(df, span=span, sample=sample)

    index, group = get_index_group(sample, False)

    both = '1' in span

    return api_formato.format_linea_hist(df_response, index, group, tipo=tipo, both=both)


@app.get('/table')
def table(user_id: int=CUSTOMER_ID):

    df_prod = get_prod(user_id)
    df_con = get_consumo(user_id)
    df_response = api_views.get_table(df_con, df_prod)
    response = df_response.to_dict(orient='records')

    return response


@app.get('/consumo_now')
def test_bot_cons(user_id: int=CUSTOMER_ID):

    df_con = get_consumo(user_id)
    df_response = api_views.data_now(df_con)
    response = df_response.to_dict(orient='records')

    return response[0]

@app.get('/produccion_now')
def test_bot_prod(user_id: int=CUSTOMER_ID):

    df = get_prod(user_id)
    df_response = api_views.data_now(df)
    response = df_response.to_dict(orient='records')

    return response[0]


@app.get('/prediccion')
def prediccion(user_id: int=CUSTOMER_ID):

    df = get_prod(user_id)

    df_response = api_views.get_prediccion(df)

    data = list(df_response['Produccion'])
    data = data[:12]
    print(len(data), data)

    predicciones = hacer_predicciones(data, CANT_PREDICCIONES)

    print(predicciones)

    return [float(x) for x in predicciones]