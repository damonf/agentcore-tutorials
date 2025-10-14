import boto3

client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')

response = client.create_agent_runtime(
    agentRuntimeName='custom_agent',
    agentRuntimeArtifact={
        'containerConfiguration': {
            'containerUri': '643917810259.dkr.ecr.us-west-2.amazonaws.com/custom-agent:latest'
        }
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn='arn:aws:iam::643917810259:role/AmazonBedrockAgentCoreSDKRuntime-us-west-2-c685a2c9ba'
)

print(f"Agent Runtime created successfully!")
print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
print(f"Status: {response['status']}")
