import pandas as pd


FILE_NAME_CSV_DATASET_CLIMA = './scraper_clima/clima_sydney_limpio2.csv'
FILE_NAME_CSV_DATASET_PRODUCCION = './dataset_produccion_energia/produccion.csv.zip'



def main():
    df_clima = pd.read_csv(FILE_NAME_CSV_DATASET_CLIMA)
    df_produccion = pd.read_csv(FILE_NAME_CSV_DATASET_PRODUCCION)


    
    
if __name__ == '__main__':
    main()    