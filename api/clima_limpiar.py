import pandas as pd
import numpy as np
import re
from clima_scraper import get_clima

DEBUG = True
FILE_NAME = './scraper_clima/clima_sydney_limpio3.csv'
VAR_CAT_N = 5

def clean_df(df_input: pd.DataFrame = None):

    if df_input is None:
        URL = 'https://raw.githubusercontent.com/PabloSGomez50/humai-solar-panels/main/scraper_clima/clima_sidney_2.csv'

        df = pd.read_csv(URL, skipinitialspace = True)
    else:
        df = df_input

    print(df.head())
    # df = df.drop(columns='Unnamed: 0')
    
    df = clean_and_convert(df)
    df['Visibility'] = df['Visibility'].interpolate(method='pad')
    # df = weather_one_hot(df)
    #df = normalizacion(df)
    df = fix_datetime(df)

    # df.to_csv(FILE_NAME)
    return df


def clean_and_convert(df_temp):

    if DEBUG:
        print('DEBUG: Limpieza y convercion de datos numericos')

    df_temp['Temp'] = df_temp['Temp'].apply(extract)
    df_temp['Wind'] = df_temp['Wind'].apply(extract)
    df_temp['Humidity'] = df_temp['Humidity'].apply(extract)
    df_temp['Barometer'] = df_temp['Barometer'].apply(extract)
    df_temp['Visibility'] = df_temp['Visibility'].apply(extract)
    df_temp = df_temp.convert_dtypes()
    df_temp['Weather'] = var_categorica(VAR_CAT_N, df_temp)
    df_temp['Weather'] = df_temp['Weather'].interpolate(method='pad')

    return df_temp.copy()


def weather_one_hot(df_temp):

    if DEBUG:
        print('DEBUG: Limpieza de la variable *Weather*')

    df_temp['Weather'] = var_categorica(VAR_CAT_N, df_temp)
    df_temp['Weather'] = df_temp['Weather'].interpolate(method='pad')

    # df_temp = df_temp.join(pd.get_dummies(df_temp['Weather']))
    #df_temp = df_temp.drop(columns='Weather')

    return df_temp.copy()


def var_categorica(n, df_temp):
    select = list(df_temp['Weather'].value_counts().head(n).index)
    serie_filtrada = df_temp['Weather'].apply(lambda x: x[:-1] if x in select else None)

    if DEBUG:
        total = df_temp['Weather'].shape[0]
        vacias = serie_filtrada.isna().sum()
        ratio = vacias * 100 / total

        print(f'\tQuedaron {vacias} filas vacias de un total de {total} filas. Un ratio de {ratio:0.2f}%')

    return serie_filtrada.copy()


def extract(string):
  """
  Limpiar una cadena de caracteres utilizando regex.
  input: pandas.Series => str
  output: pandas.Series => int || str(sin convertir)
  extra: 
    'No wind' => 0
    '('N/A',)' => np.NAN
  """
  number = re.search(r'(\d+)', str(string))

  if number is not None:
    return int(number.group())

  else:
    if string == 'No wind':
      return 0

    if string == "('N/A',)":
      return np.NAN

    return string


def normalize_df(df_temp):
    return df_temp.apply(lambda x: (x - x.mean()) / x.std(), axis=0)

def normalizacion(df_temp):
    """
    Normalizacion de las variables numericas para utilizar en modelos de ML
    """

    if DEBUG:
        print('DEBUG: Normalizacion de datos numericos')

    df_temp.loc[:,'Temp':'Visibility'] = normalize_df(df_temp.loc[:,'Temp':'Visibility'])

    return df_temp.copy()


def fix_datetime(df_temp):
    """
    Usar la columna Date y Hour para generar una sola columna que contenga objetos datetime 
    """
    if DEBUG:
        print('DEBUG: Creando la variable datetime')

    df_temp['Date'] = df_temp['Date'] + df_temp['Hour']
    df_temp['Datetime'] = pd.to_datetime(df_temp['Date'], format='%Y-%m-%d%H:%M')
    df_temp.drop(columns=['Hour', 'Date'], inplace=True)
    df_temp.set_index('Datetime', inplace=True)

    return df_temp.copy()



if __name__ == '__main__':
    df_init = get_clima()
    df_final = clean_df(df_init)
    # df_final.to_csv('clima.csv')
    print(df_final.head())