from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_utils import consumo_last_7d

app = FastAPI()

origins = [
    'http://127.0.0.1:5173'
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])



@app.get('/')
def root():

    return {'message': 'Hello World'}



@app.get('/data')
def total_diario():

    response = consumo_last_7d(1)

    return response