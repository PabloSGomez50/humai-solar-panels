import pandas as pd


FILE_NAME_CSV_DATASET_CLIMA = './scraper_clima/clima_sydney_limpio2.csv'
FILE_NAME_CSV_DATASET_PRODUCCION = './dataset_produccion_energia/produccion.csv.zip'


def get_dataset_clima():
    df_clima = pd.read_csv(FILE_NAME_CSV_DATASET_CLIMA)
    df_clima.drop(columns=['Unnamed: 0'], inplace = True)
    df_clima.rename(columns={'Date': 'Datetime'}, inplace = True)    
    return df_clima

def get_dataset_produccion():
    df_produccion = pd.read_csv(FILE_NAME_CSV_DATASET_PRODUCCION)
    df_produccion.rename(columns={'datetime': 'Datetime'}, inplace = True)
    return df_produccion

def join_dataset(df_clima, df_produccion, customer_id):
    df_produccion_only_one_customer = df_produccion[df_produccion.Customer == customer_id]
    df_produccion_only_one_customer.drop(columns='Customer', inplace = True)
    df_join = df_produccion_only_one_customer.merge(df_clima, left_on="Datetime", right_on="Datetime", how="left")
    df_join.sort_values(by ='Datetime', inplace=True)
    df_join.fillna(method = 'ffill', inplace = True)
    return df_join
    
def main():
    df_clima = get_dataset_clima()
    df_produccion = get_dataset_produccion()
    df_join = join_dataset(df_clima, df_produccion, 1)

    print(df_join.head())

   
    
if __name__ == '__main__':
    main()    