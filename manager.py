from aws_utils import aws_s3
from scraper_clima.scraper_clima import get_clima


S3_NAME = 'clima_sidney_scraped.csv'

if __name__ == '__main__':
    # Pedir el clima

    df_clima = get_clima()

    aws_s3.send_object_s3(S3_NAME, df_clima)
    