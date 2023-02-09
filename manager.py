from aws_utils import aws_s3
from scraper_clima.scraper_clima import get_clima
from script_produccion.limpiar_prod import get_prod_customer

S3_CLIMA_NAME = 'clima_sidney_scraped.csv'

def send_clima():

    df_clima = get_clima()

    aws_s3.send_object_s3(S3_CLIMA_NAME, df_clima)

    print(f'DEBUG: se envio exitosamente el archivo {S3_CLIMA_NAME}')

def send_prod(id):

    df_prod = get_prod_customer(id)
    name = f'produccion/user_{id}.csv'

    aws_s3.send_object_s3(name, df_prod)
    print(f'DEBUG: se envio exitosamente el archivo {name}')

if __name__ == '__main__':
    """
    Test de funciones
    """

    print('DEBUG: Este archivo se encarga de generar dataframes y enviarlos al bucket en aws')
    # send_clima()
    send_prod(5)
    