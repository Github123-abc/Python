import boto3

client = boto3.client('iam')

response = client.list_users()

users = response['Users']

print('All account users')

for user in users:
    print(f'  - {user["UserName"]}')