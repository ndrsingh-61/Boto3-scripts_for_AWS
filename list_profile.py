import boto3

iam_console = boto3.resource('iam')

for user in iam_console.users.all():
    print(user.name)