import boto3

client = boto3.client('ec2', region_name='us-west-2')


response = client.run_instances(

    ImageId='ami-0b55e9f47df6db826',
    InstanceType='t1.micro',
    KeyName='test',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[
        'sg-085fa936196e438d4',
    ],

)



