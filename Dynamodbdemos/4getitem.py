import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = dynamodb.Table('users')

response = table.get_item(
    Key={
        'username': 'Pebbles',
        'last_name': 'Flintstone'
    }
)
item = response['Item']
print(item)