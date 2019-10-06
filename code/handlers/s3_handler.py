import pandas as pd

from io import StringIO
import boto3

from constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from constants import BUCKET_NAME, APARTMENTS_FILENAME

from handlers.requests_helper import request_with_retry


def basic_write_to_s3(df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.Object(BUCKET_NAME, APARTMENTS_FILENAME).put(Body=csv_buffer.getvalue())


def write_to_s3(df):
    request_with_retry(basic_write_to_s3, 15, df)


def basic_read_from_s3():
    s3 = boto3.client('s3',  aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    csv_object = s3.get_object(Bucket=BUCKET_NAME, Key=APARTMENTS_FILENAME)
    body = csv_object['Body']
    csv_string = body.read().decode('utf-8')
    return pd.read_csv(StringIO(csv_string))


def read_from_s3():
    return request_with_retry(basic_read_from_s3, 15)
