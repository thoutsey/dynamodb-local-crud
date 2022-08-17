import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = dynamodb.Table('users')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'username': 'Fred',
            'first_name': 'Fred',
            'last_name': 'Flintstone',
         
          
        }
    )
    batch.put_item(
        Item={
            'username': 'Wilma',
            'first_name': 'Wilma',
            'last_name': 'Flintstone',
            'age': 40
        }
    )
    batch.put_item(
        Item={
            'username': 'Kitty',
            'first_name': 'Evil',
            'last_name': 'Secret',
            'FavoriteThings':['Pick on Max the pup','Plotting to take over the world']
        }
    )
    print('Batch has been added')