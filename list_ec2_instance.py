import boto3   

#using resource
ec2_instance = boto3.resource('ec2')
for instance in ec2_instance.instances.all():
    print(instance.id)



#using client
ec2_client = boto3.client('ec2')
myec2 = ec2_client.describe_instances()

for instance in myec2['Reservations']:
    print(instance)
