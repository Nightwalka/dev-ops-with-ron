
import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='this-is-from-boto'
    
)

print(response)







# import boto3

# client = boto3.client('s3')
# response = client.create_bucket(
 
#     Bucket='this-is-from-boto',

# )