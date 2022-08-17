import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

from boto3.dynamodb.conditions import Key, Attr

table = dynamodb.Table('users')

response = table.query(
        KeyConditionExpression=Key('username').eq('Kitty')
    )
items = response['Items']
print(items)