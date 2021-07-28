import boto3

client = boto3.client('glue')


def lambda_handler(event, context):
    crawler_name = event['crawler_name']

    response = client.get_crawler(Name=crawler_name)

    # 'READY'|'RUNNING'|'STOPPING'
    status = response['Crawler']['State']

    return status
