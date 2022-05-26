import boto3

# Creating a Dynamodb Table

table = boto3.client("dynamodb")
movie = table.create_table(TableName='Movies',
                           KeySchema=[
                               {'AttributeName': 'Year',
                                'KeyType': 'HASH'},  # Partition Key
                               {'AttributeName': 'Title',
                                'KeyType': 'RANGE'}],  # Sort Key
                           AttributeDefinitions=[
                               {'AttributeName': 'Year',
                                'AttributeType': 'N'},
                               {'AttributeName': 'Title',
                                'AttributeType': 'S'}
                           ],
                           ProvisionedThroughput={
                               'ReadCapacityUnits': 10,
                               'WriteCapacityUnits': 10}
                           )
print(movie)
