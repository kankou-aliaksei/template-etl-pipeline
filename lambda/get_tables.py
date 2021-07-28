import os
import boto3

client = boto3.client('glue')

DB_NAME = os.environ.get('DB_NAME')


def lambda_handler(event, context):
    tablesResponse = client.get_tables(DatabaseName=DB_NAME)

    table_list = tablesResponse['TableList']

    tables = []
    for table in table_list:
        tables.append(table['Name'])

    return tables
