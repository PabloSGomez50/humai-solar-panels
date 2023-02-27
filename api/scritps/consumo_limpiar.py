import pandas as pd

PATH_LOCAL = '../data/solar.parquet'
CUSTOMER_ID = 1
DEBUG = True


def get_df_consumo(user_id: int):
    """
    Funcion para limpiar el dataset de los paneles
    Devuelve el consumo del cliente *CUSTOMER_ID*

    Columnas: Datetime | GC | CL | Total
    """
    
    df = pd.read_parquet(PATH_LOCAL, engine='pyarrow')
    if DEBUG:
        print('Leyo el archivo')
    # Limpiar las columnas y hacer el melt
    df = drop_columns(df, user_id)

    if 'CL' in df['cat'].unique():
        df = cl_gc_column(df)
    else:
        df = df.rename(columns={'consumo': 'GC'}).drop('cat', axis=1)
        df['Total'] = df['GC'].copy()

    df = format_date(df)

    return df


def drop_columns(df_, user_id):
    """
    Selecciona el cliente, realiza el melt y elimina todas las columnas extra
    """
    if DEBUG:
        print('DEBUG: funcion drop_columns')

    df_temp = df_[df_['Customer'] == user_id]
    # df_temp = df_temp.drop(columns=['Postcode', 'Row Quality', 'Generator Capacity', 'Customer'])
    df_temp = df_temp.drop(columns=['Customer'])

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
    # df_ = df_.loc[:,::-1]
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

    df_temp = df_[df_['cat'] == 'GC'].copy()

    df_temp.rename(columns={'consumo': 'GC'}, inplace=True)
    df_temp.drop(columns='cat', inplace=True)
    df_temp.reset_index(drop=True, inplace=True)

    serie_cl = df_[df_['cat'] == 'CL']['consumo'].copy()
    df_temp['CL'] = serie_cl.reset_index(drop=True)
    
    df_temp['Total'] = df_temp['GC'] + df_temp['CL']

    return df_temp.copy()


if __name__ == '__main__':

    df = get_df_consumo(CUSTOMER_ID)
    # df.to_csv(f'./consumo_user_{CUSTOMER_ID}.csv')

    message = """En este script de python se accede al dataset completo y seleccion un customer.
        Se devuelve un dataset:
        Columnas: datetime | GC | CL | total
        """
    print(message)
    print(df.sample(10))
    # df.to_csv('test.csv')