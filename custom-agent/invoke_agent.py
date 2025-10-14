import boto3
import json

agent_core_client = boto3.client('bedrock-agentcore', region_name='us-west-2')
payload = json.dumps({
    "input": {"prompt": "Explain machine learning in simple terms"}
})

response = agent_core_client.invoke_agent_runtime(
    # TODO: replace with your actual ARN from deploy_agent.py output
    agentRuntimeArn='arn:aws:bedrock-agentcore:us-west-2:643917810259:runtime/custom_agent-JlPhWQDRRa',
    runtimeSessionId='dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt',  # Must be 33+ chars
    payload=payload,
    qualifier="DEFAULT"
)

response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)
