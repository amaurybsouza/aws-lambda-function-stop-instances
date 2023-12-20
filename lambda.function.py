"""
Make sure to replace the placeholder values in instance_ids with the actual IDs of the EC2 instances you want to stop.
"""
import boto3

def lambda_handler(event, context):
    # Set your AWS region
    region = 'us-east-1'

    # Create an EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    # Specify the instance IDs you want to stop
    instance_ids = ['i-1234567890abcdef0', 'i-abcdef01234567890']

    # Stop the specified instances
    response = ec2_client.stop_instances(InstanceIds=instance_ids)

    # Log the response
    print(response)

    return {
        'statusCode': 200,
        'body': 'Instances stopped successfully!'
    }
