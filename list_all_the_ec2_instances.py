import boto3 
from pprint import pprint  #to describe the instance in a proper json format
aws_mng_con = boto3.session.Session()
aws_ec2_inst = aws_mng_con.resource(service_name = 'ec2', region_name = 'us-east-1')
cnt = 1
for each in aws_ec2_inst.instances.all():
    print(cnt, each, each.instance_id, each.instance_type, each.launch_time.strftime("%y-%m-%d"), each.private_ip_address)
    cnt += 1

# response = aws_ec2_inst.describe_instances()
# pprint(response)

