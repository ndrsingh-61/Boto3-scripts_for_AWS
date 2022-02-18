from urllib import response
import boto3
s3_resource = boto3.resource(service_name = 's3')

bucket= s3_resource.Bucket("firsts3boto3bucket-01")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)
print(response)