from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import api_views
import api_formato

CSV_CONSUMO = './consumo_user_{0}.csv'
CSV_PROD = './user_{0}.csv'

app = FastAPI()

origins = [
    'http://127.0.0.1:5173'
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event('startup')
def start_app():
    print('Es re flashero que pueda ejecutar funciontes de esta manera')
    print('Y tambien de esta manera ')


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


@app.get('/')
def root():

    return {'message': 'Hello World'}



@app.get('/consumo')
def consumo_7d():

    df = get_consumo(1)
    df_response = api_views.consumo_last_7d(df)
    response = api_formato.format_summary(df_response)

    return response


@app.get('/cards')
def resumen():

    df = get_prod(1)
    response = api_views.prod_last_7(df)

    return response


@app.get('/calendar/{year}')
def calendario(year: int):

    df = get_prod(1)
    df_response = api_views.prod_calendar(df, year)
    response = api_formato.format_calendario(df_response)

    return response


@app.get('/line/{span}/{sample}')
def historia(span: str ='1M', sample: str ='1D'):

    df = get_prod(1)
    df_response = api_views.prod_history(df, span=span, sample=sample)

    if sample.endswith('W'):
        response = api_formato.format_linea_hist(df_response, index='%m-%d', group='%Y')

    elif sample.endswith('D'):
        response = api_formato.format_linea_hist(df_response, index='%d', group='%m')
        
    elif sample.endswith('H'):
        response = api_formato.format_linea_hist(df_response, index='%d %H:%M', group='%m')

    else:
        response = api_formato.format_linea_hist(df_response, index='%H:%M', group='%d')

    return response


@app.get('/table')
def table():

    df_prod = get_prod(1)
    df_con = get_consumo(1)
    df_response = api_views.get_table(df_con, df_prod)
    response = df_response.to_dict(orient='records')

    return response


@app.get('/consumo_now')
def test_bot():

    df_response = api_views.consumo_now(1)
    response = df_response.to_dict(orient='records')

    return response[0]