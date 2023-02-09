import boto3
from dotenv import load_dotenv
from io import StringIO
import os

load_dotenv()

BUCKET_NAME = 'humai-solar-project'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

if AWS_ACCESS_KEY_ID is None or AWS_SECRET_ACCESS_KEY is None:
    raise ValueError('Faltan Keys en el archivo .env')

def get_bucket():
    """
    Valida las credenciales y devuelve el Bucket
    """
    s3 = boto3.resource('s3', 
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                        )
    return s3.Bucket(BUCKET_NAME)

def create_file(df):
    """
    Convierte un dataframe en el archivo para subir a AWS S3
    """
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)

    return csv_buffer.getvalue()


def send_object_s3(name, df):
    """
    Subir un archivo a S3
    """
    
    bucket = get_bucket()
    csv_file = create_file(df)

    bucket.put_object(Body=csv_file, Key=name)


def get_list():
    """
    Lista de los archivos cargados en el bucket
    Output: dict [str]
    """
    bucket = get_bucket()

    return [x.key for x in bucket.objects.all()]

if __name__ == '__main__':
    print()
    print('DEBUG: Este archivo permite trabajar con AWS S3')
    print()
    