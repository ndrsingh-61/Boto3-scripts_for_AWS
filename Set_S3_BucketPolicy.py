import boto3
import json

s3_client = boto3.client(service_name = 's3')
s3_policy = s3_client.get_bucket_policy(Bucket='firsts3boto3bucket-01')
json_str = json.dumps(s3_policy)
print(json_str)
