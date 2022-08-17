import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = dynamodb.Table('users')

table.put_item(
   Item={
        'username': 'Pebbles',
        'first_name': 'Pebbles',
        'last_name': 'Flintstone',
        'age': 25,
        'favorites':{'pets':'Dyno','Codeing Language':'Hammer & Chizzle'},
        'places':['Quarry','Beach','Bedrock'],
        'friend':['bambam']
    }
    )
    

    
response = table.get_item(
    Key={
        'username': 'Pebbles',
        'last_name': 'Flintstone'
    }
    )
item= response['Item']
print(item, 'has been created')
    
