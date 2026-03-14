import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    name = body['name']
    email = body['email']

    table.put_item(
        Item={
            'id': str(uuid.uuid4()),
            'name': name,
            'email': email
        }
    )

    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps('Data saved')
    }