import boto3

# Adding Movies to the table

table = boto3.client("dynamodb")
first = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2014'},
                        'Title': {'S': 'Interstellar'},
                        'Rating': {'N': '9.8'}
                        })
second = table.put_item(TableName='Movies',
                        Item=
                        {'Year': {'N': '2017'},
                         'Title': {'S': 'Logan'},
                         'Rating': {'N': '7.8'}
                         })
third = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2021'},
                        'Title': {'S': 'Malignant'},
                        'Rating': {'N': '6'}
                        })
forth = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2021'},
                        'Title': {'S': 'Externals'},
                        'Rating': {'N': '8'}
                        })
fifth = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2019'},
                        'Title': {'S': 'TAG'},
                        'Rating': {'N': '7.8'}
                        })
sixth = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2016'},
                        'Title': {'S': 'Batman VS Superman'},
                        'Rating': {'N': '8'}
                        })
seventh = table.put_item(TableName='Movies',
                         Item=
                         {'Year': {'N': '2022'},
                          'Title': {'S': 'Jackass'},
                          'Rating': {'N': '6.5'}
                          })
eighth = table.put_item(TableName='Movies',
                        Item=
                        {'Year': {'N': '2010'},
                         'Title': {'S': 'Avatar'},
                         'Rating': {'N': '9.2'}
                         })
ninth = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2008'},
                        'Title': {'S': 'Twilight'},
                        'Rating': {'N': '8.5'}
                        })
tenth = table.put_item(TableName='Movies',
                       Item=
                       {'Year': {'N': '2018'},
                        'Title': {'S': 'Hereditary'},
                        'Rating': {'N': '9.5'}
                        })
print(first)
print(second)
print(third)
print(forth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(ninth)
print(tenth)