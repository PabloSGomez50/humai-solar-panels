import pandas as pd

URL = 'https://humai-solar-project.s3.amazonaws.com/2012-2013_Solar_data.csv'
PATH_LOCAL = '../script_produccion/2012-2013 Solar home electricity data v2.csv.zip'
CUSTOMER_ID = 1
DEBUG = True

def drop_columns(df_):
    """
    Selecciona el cliente, realiza el melt y elimina todas las columnas extra
    """
    if DEBUG:
        print('DEBUG: funcion drop_columns')

    df_temp = df_[df_['Customer'] == CUSTOMER_ID]
    df_temp = df_temp.drop(columns=['Postcode', 'Row Quality', 'Generator Capacity', 'Customer'])

    df_temp = df_temp[df_temp['Consumption Category'] != 'GG']
    df_temp = df_temp.rename(columns={'Consumption Category': 'cat'})
    df_temp = df_temp.melt(id_vars=['cat', 'date'], var_name='time', value_name='consumo')

    return df_temp.copy()


def format_date(df_):
    """
    Formate el dataframe con la fecha correcta y arregla el orden de las columnas
    """

    if DEBUG:
        print('DEBUG: funcion format_date')

    df_['Datetime'] = pd.to_datetime(df_['date'] + df_['time'], format='%d/%m/%Y%H:%M')
    df_.drop(columns=['date', 'time'], inplace=True)
    df_ = df_.loc[:,::-1]
    df_.sort_values('Datetime', inplace=True)
    df_.set_index('Datetime', inplace=True)

    return df_.copy()


def cl_gc_column(df_):
    """
    Funcion que trabaja con el df con el melt aplicado.
    transforma la columna categoria en dos columnas independientes
    """

    if DEBUG:
        print('DEBUG: funcion cl_gc_column')

    df_temp = df_[df_['cat'] == 'CL'].copy()
    serie_gc = df_[df_['cat'] == 'GC']['consumo'].copy()

    df_temp.rename(columns={'consumo': 'CL'}, inplace=True)
    df_temp.drop(columns='cat', inplace=True)
    df_temp.reset_index(drop=True, inplace=True)

    df_temp['GC'] = serie_gc.reset_index(drop=True)

    return df_temp.copy()


def get_df_consumo():
    """
    Funcion para limpiar el dataset de los paneles
    Devuelve el consumo del cliente *CUSTOMER_ID*

    Columnas: Datetime | GC | CL | Total
    """

    if DEBUG:
        print('DEBUG: funcion get_df_consumo')
        df = pd.read_csv(PATH_LOCAL, header = [1])
    else:
        df = pd.read_csv('https://humai-solar-project.s3.amazonaws.com/2012-2013_Solar_data.csv')
        
    print('Leyo el archivo')
    # Limpiar las columnas y hacer el melt
    df = drop_columns(df)

    df = cl_gc_column(df)

    df = format_date(df)

    df['Total'] = df['GC'] + df['CL']

    return df


if __name__ == '__main__':

    df = get_df_consumo()
    # df.to_csv(f'./consumo_user_{CUSTOMER_ID}.csv')

    message = """En este script de python se accede al dataset completo y seleccion un customer.
        Se devuelve un dataset:
        Columnas: datetime | GC | CL | total
        """
    print(message)
    print(df.sample(10))
    # df.to_csv('test.csv')