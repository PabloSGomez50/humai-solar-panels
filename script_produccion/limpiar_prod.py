import pandas as pd

FILE_NAME_ZIP_SOLAR_HOME = './2012-2013 Solar home electricity data v2.csv.zip'
FILE_NAME_ZIP_SOLAR_GLOBAL = './script_produccion/2012-2013 Solar home electricity data v2.csv.zip'
URL = 'https://humai-solar-project.s3.amazonaws.com/2012-2013_Solar_data.csv'
CUSTOMER_ID = 1
DEBUG = True

def get_prod_customer(customer_id: int = CUSTOMER_ID):
    """
    Funcion para limpiar el dataset de los paneles
    Devuelve la produccion del cliente *customer_id*

    Columnas: Datetime | Produccion
    """

    if DEBUG:
        try:
            df = pd.read_csv(FILE_NAME_ZIP_SOLAR_HOME, header = [1])
            print('DEBUG: Se creo el dataframe')
        except FileNotFoundError:
            df = pd.read_csv(FILE_NAME_ZIP_SOLAR_GLOBAL, header = [1])
            print('DEBUG: Se creo el dataframe')
    else:
        df = pd.read_csv(URL)

    # Nos quedamos solo con la categoría 'GG'
    df = df[df['Consumption Category'] == 'GG']
    # Eliminamos el resto de columnas
    df = df.drop(['Generator Capacity','Postcode','Consumption Category','Row Quality'], axis = 1)

    # Seleccionamos el curstomer
    df = df[df['Customer'] == customer_id]

    # Simplificamos las columnas de horas en Produccion
    df_ = df.melt(id_vars = ['Customer', 'date'], value_name='Produccion')

    # Pasar a datetime y ordenar valores
    df_['Datetime'] = pd.to_datetime(df_['date'] + df_['variable'], format='%d/%m/%Y%H:%M')
    df_.sort_values(['Datetime'], inplace = True)
    
    # Arreglar indices ylas columnas restantes 
    df_ = df_.drop(columns=['date', 'variable', 'Customer'])
    df_.reset_index(drop=True, inplace=True)
    df_ = df_.loc[:,::-1]

    return df_


if __name__ == '__main__':
    
     df = get_prod_customer()

     print('\nDEBUG: 10 datos del Dataframe resultante:')
     print(df.sample(10))