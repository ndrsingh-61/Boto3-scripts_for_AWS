import boto3

def create_ec2_instace():
    try:
            ec2_instance = boto3.client('ec2')
            ec2_instance.run_instances(
                ImageId        = "ami-08e4e35cccc6189f4",
                MinCount        = 1,
                MaxCount        = 1,
                InstanceType    = "t2.micro",
                KeyName         = "ec2-key"
        )
    except Exception as e:
        print(e)   

def describe_ec2_instance():
    try:
        ec2_instance = boto3.client('ec2')
        return str(ec2_instance.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)


def stop_ec2_instance():
    try:
        ec2_instance = boto3.client('ec2')
        instance_id = describe_ec2_instance()
        ec2_instance.stop_instances(InstanceIds =[instance_id])
    except Exception as e:
        print(e)  

def start_ec2_instance():
    try:
        ec2_instance = boto3.client('ec2')
        instance_id = describe_ec2_instance()
        ec2_instance.start_instances(InstanceIds = [instance_id])
    except Exception as e:
        print(e)    
# create_ec2_instace()
# describe_ec2_instance()
# stop_ec2_instance()
start_ec2_instance()