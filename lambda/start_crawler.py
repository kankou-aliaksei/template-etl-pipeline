import boto3

client = boto3.client('glue')


def lambda_handler(event, context):
    crawler_name = event['crawler_name']

    response = client.start_crawler(Name=crawler_name)

    request_id = response['ResponseMetadata']['RequestId']

    return {
        'request_id': request_id
    }
