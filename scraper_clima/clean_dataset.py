import pandas as pd
import numpy as np
import re
from IPython.display import display

def main():
    URL = 'https://raw.githubusercontent.com/PabloSGomez50/humai-solar-panels/main/scraper_clima/clima_sidney_2.csv'

    df = pd.read_csv(URL, skipinitialspace = True)
    df = df.drop(columns='Unnamed: 0')
    
    df = clean_and_convert(df)
    df = normalizacion(df)

    df.to_csv('./clima_sydney_limpio.csv')


def clean_and_convert(df):
    df['Temp'] = df['Temp'].apply(extract)
    df['Wind'] = df['Wind'].apply(extract)
    df['Humidity'] = df['Humidity'].apply(extract)
    df['Barometer'] = df['Barometer'].apply(extract)
    df['Visibility'] = df['Visibility'].apply(extract)
    df = df.convert_dtypes()

    return df

def extract(string):
  
  number = re.search(r'(\d+)', str(string))
  if number is None:
    if string == 'No wind':
      return 0

    if string == "('N/A',)":
    #   print(np.NAN)
      return np.NAN

    # print(string)
    return string

  else:
    return int(number.group())

def normalizacion(df):
    df['Humidity'] = df['Humidity'] / 100
    return df

def fix_datetime(df):

    df['Date'] = df['Date'] + df['Hour']
    df = df.drop(columns='Hour')
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d%H:%M')

    return df

if __name__ == '__main__':
    main()