import boto3
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')

table.update_item(
    Key={
        'username': 'Pebbles',
        'last_name': 'Flintstone'
    },
    UpdateExpression='REMOVE age',

)
response = table.get_item(
    Key={
        'username': 'Pebbles',
        'last_name': 'Flintstone'
    }
    )
item= response['Item']
print(item, 'age has been removed')