from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api_views
import api_formato

app = FastAPI()

origins = [
    'http://127.0.0.1:5173'
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])



@app.get('/')
def root():

    return {'message': 'Hello World'}



@app.get('/consumo')
def consumo_7d():

    df_response = api_views.consumo_last_7d(1)
    response = api_formato.format_bar(df_response)

    return response


@app.get('/cards')
def resumen():

    response = api_views.prod_last_7(1)

    return response


@app.get('/prod')
def calendario():

    df_response = api_views.prod_calendar(1)
    response = api_formato.format_calendario(df_response)

    return response


@app.get('/months')
def prod_by_month():

    df_response = api_views.prod_by_month(1)
    response = api_formato.format_linea(df_response)

    return response

@app.get('/line/{span}')
def historia(span='1D'):

    df_response = api_views.prod_history(1)
    response = api_formato.format_linea(df_response)

    return response

@app.get('/table')
def table():

    df_response = api_views.get_table(1)
    response = df_response.to_dict(orient='records')

    return response