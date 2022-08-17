import boto3

from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = dynamodb.Table('users')

response = table.scan(
    FilterExpression=Attr('last_name').lt('Flintstones')
)
items = response['Items']
print(items)