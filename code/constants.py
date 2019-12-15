import os

from dotenv import load_dotenv

load_dotenv()

USE_S3 = False

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

TELEGRAM_TOKEN = os.getenv("QUINTO_ANDAR_TELEGRAM_TOKEN")
TELEGRAM_SINGLE_USER_CHAT_ID = os.getenv('SINGLE_USER_CHAT_ID')

BUCKET_NAME = 'my-favorite-public-bucket'
APARTMENTS_FILENAME = 'apartments.csv'

LOCAL_PATH = './data/local_bucket'
