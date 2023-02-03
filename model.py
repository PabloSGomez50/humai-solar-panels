import pandas as pd


FILE_NAME_CSV_DATASET_CLIMA = './scraper_clima/clima_sydney_limpio3.csv'
FILE_NAME_CSV_DATASET_PRODUCCION = './dataset_produccion_energia/produccion.csv.zip'


def get_dataset_clima():
    df_clima = pd.read_csv(FILE_NAME_CSV_DATASET_CLIMA)
    df_clima.drop(columns=['Unnamed: 0'], inplace = True)
    df_clima.rename(columns={'Date': 'Datetime'}, inplace = True)    
    
    # elimino dos registros que estaban duplicados
    dupli_1_index = df_clima[(df_clima.Datetime == '2013-04-07 02:00:00') & (df_clima.Barometer == 1023)].index
    dupli_2_index = df_clima[(df_clima.Datetime == '2013-04-07 02:30:00') & (df_clima.Barometer == 1023)].index
    df_clima = df_clima.drop(df_clima.index[dupli_1_index]).drop(df_clima.index[dupli_2_index]) 
    
    return df_clima

def get_dataset_produccion():
    df_produccion = pd.read_csv(FILE_NAME_CSV_DATASET_PRODUCCION)
    df_produccion.rename(columns={'datetime': 'Datetime'}, inplace = True)
    return df_produccion

def join_dataset(df_clima, df_produccion, customer_id):

    # me quedo con un unico customer_id
    df_produccion_only_one_customer = df_produccion[df_produccion.Customer == customer_id]
    df_produccion_only_one_customer.drop(columns='Customer', inplace = True)

    # luego de este join van a aparecer muchos registros con los datos del clima en NaN
    df_join = df_produccion_only_one_customer.merge(df_clima, left_on="Datetime", right_on="Datetime", how="left")

    # casteo la fecha para que sea datatime
    df_join['Datetime'] = pd.to_datetime(df_join['Datetime'], format='%Y-%m-%d %H:%M:%S')

    # Ordeno el dataset para que la imputacion por el valor anterior funcione correctamente
    df_join.sort_values(by ='Datetime', inplace=True)
    df_join.fillna(method = 'ffill', inplace = True)

    # Seteo la fecha como index y establezco la frecuencia    
    df_join.set_index("Datetime", inplace=True)
    df_join = df_join.asfreq('30T')
    
    return df_join
    
def main():
    df_clima = get_dataset_clima()
    df_produccion = get_dataset_produccion()
    df_join = join_dataset(df_clima, df_produccion, 1)

    print(df_join.head())

   
    
if __name__ == '__main__':
    main()    