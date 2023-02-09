from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api_utils

app = FastAPI()

origins = [
    'http://127.0.0.1:5173'
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])



@app.get('/')
def root():

    return {'message': 'Hello World'}



@app.get('/consumo')
def total_diario():

    response = api_utils.consumo_last_7d(1)

    return response


@app.get('/prod')
def produccion(span='1d'):

    response = api_utils.prod_history(span)

    return response


@app.get('/months')
def produccion():

    response = api_utils.prod_by_month()

    return response