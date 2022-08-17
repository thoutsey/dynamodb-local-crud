import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = dynamodb.Table('users')

table.delete()

print('Table has been deleted')