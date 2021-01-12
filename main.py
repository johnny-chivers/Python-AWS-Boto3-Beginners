'''
Python Code for Johnny Chivers Beginners Guide To Python For AWS

The # character commends out the code
'''
import boto3

s3_client = boto3.client('s3')

s3_client.create_bucket(Bucket="johnny-chivers-test-1-boto", CreateBucketConfiguration={'LocationConstraint':'eu-west-1'})

response = s3_client.list_buckets()

print(response)

