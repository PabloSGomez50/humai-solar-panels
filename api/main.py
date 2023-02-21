from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import os 
from datetime import datetime, timedelta

import api_views
import api_formato
import clima_scraper
import clima_limpiar

CSV_CONSUMO = './consumo_user_{0}.csv'
CSV_PROD = './user_{0}.csv'
CSV_CLIMA = './clima_{0}_{1}.csv'
DAYS_DIFF = 2 + 365 * 10
CUSTOMER_ID = 1

app = FastAPI()

origins = [
    'http://127.0.0.1:5173',
    'https://humai-solar-panels.vercel.app'
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



@app.get('/consumo')
def consumo_last_7d():

    df = get_consumo(CUSTOMER_ID)
    df_response = api_views.consumo_last_7d(df)
    response = api_formato.format_summary(df_response)

    return response


@app.get('/prod')
def resumen():

    df = get_prod(CUSTOMER_ID)
    df_response = api_views.prod_last_7(df)
    response = api_formato.format_summary(df_response)
    
    return response


@app.get('/clima')
def show_clima():

    today = datetime.today()
    df_clima = pd.read_csv(CSV_CLIMA.format(today.month, today.day), parse_dates=['Datetime'])

    df_clima.sort_index(ascending=False, inplace=True)

    response = api_formato.format_clima(df_clima)
    
    return response


@app.get('/summary')
def summary():

    df_con = get_consumo(CUSTOMER_ID)
    df_prod = get_prod(CUSTOMER_ID)

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
def horas():
    df = get_prod(CUSTOMER_ID)
    df_response = api_views.horas(df)
    response = df_response.to_dict(orient='records')
    # response = api_formato.format_summary(df_response)

    return response
    

@app.get('/calendar/{year}')
def calendario(year: int):

    df = get_prod(CUSTOMER_ID)
    df_response = api_views.prod_calendar(df, year)
    response = api_formato.format_calendario(df_response)

    return response


@app.get('/line/{span}/{sample}')
def historia(span: str ='1M', sample: str ='1D', telegram: bool = False):

    df = get_prod(CUSTOMER_ID)
    df_response = api_views.prod_history(df, span=span, sample=sample)

    print(telegram, type(telegram))

    if sample.endswith('W'):
        index = '%m-%d'
        group='%Y'

    elif sample.endswith('D'):
        index='%d'
        group='%m'
        
    elif sample.endswith('H'):
        index='%d'
        group='%m'

    else:
        index='%H:%M'
        group='%d'

    if telegram:
        return api_formato.format_linea_telegram(df_response, index, group)
    
    else:
        return api_formato.format_linea_hist(df_response, index, group)

@app.get('/table')
def table():

    df_prod = get_prod(CUSTOMER_ID)
    df_con = get_consumo(CUSTOMER_ID)
    df_response = api_views.get_table(df_con, df_prod)
    response = df_response.to_dict(orient='records')

    return response


@app.get('/consumo_now')
def test_bot_cons():

    df_con = get_consumo(CUSTOMER_ID)
    df_response = api_views.data_now(df_con)
    response = df_response.to_dict(orient='records')

    return response[0]

@app.get('/produccion_now')
def test_bot_prod():

    df = get_prod(CUSTOMER_ID)
    df_response = api_views.data_now(df)
    response = df_response.to_dict(orient='records')

    return response[0]