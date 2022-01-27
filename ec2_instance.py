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

create_ec2_instace()