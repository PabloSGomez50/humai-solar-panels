import pandas as pd
from pathlib import Path
import zipfile

FILE_NAME_ZIP_SOLAR_HOME = './dataset_produccion_energia/2012-2013 Solar home electricity data v2.csv.zip'
FILE_NAME_ZIP_SOLAR_HOME = './2012-2013 Solar home electricity data v2.csv.zip'


def save_compressed_df(df, dirPath, fileName):
    """Save a Pandas dataframe as a zipped .csv file.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Input dataframe.
    dirPath : str or pathlib.PosixPath
        Parent directory of the zipped file.
    fileName : str
        File name without extension.
    """

    dirPath = Path(dirPath)
    path_zip = dirPath / f'{fileName}.csv.zip'
    txt = df.to_csv(index=False)
    with zipfile.ZipFile(path_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f'{fileName}.csv', txt)
        
        
def main():
    df = pd.read_csv(FILE_NAME_ZIP_SOLAR_HOME, header = [1])

    df = df[df['Consumption Category'] == 'GG'] #nos quedamos solo con la categoría 'GG'
    df = df.drop(['Generator Capacity','Postcode','Consumption Category','Row Quality'], axis = 1)

    #df = df[df['Customer'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])] #filtro solo los primeros 10 clientes
    #df = df[df['Customer'] == 1]

    df_ = df.melt(id_vars = ['Customer', 'date'])

    df_['datetime'] = df_['date'] + ' ' + df_['variable']

    df_['datetime'] = pd.to_datetime(df_['datetime'], format='%d/%m/%Y %H:%M')

    df_ = df_.drop(columns=['date', 'variable'])
    df_ = df_.rename(columns={'value': 'Produccion'})
    df_.sort_values(['Customer','datetime'], inplace = True)

    # print(df_.head())
    # df_.to_csv('produccion.csv')
    save_compressed_df(df_, './dataset_produccion_energia','produccion')
    
    
    
if __name__ == '__main__':
    main()        