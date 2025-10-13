# test client to invoke the agent
import json
import boto3
  
# Get the ARN from .bedrock-agentcore.yaml
agent_arn = "arn:aws:bedrock-agentcore:us-west-2:643917810259:runtime/yellow-03ZIWi64Er"
prompt = "Tell me a joke"

# Initialize the AgentCore client
agent_core_client = boto3.client('bedrock-agentcore')
  
# Prepare the payload
payload = json.dumps({"prompt": prompt}).encode()
  
# Invoke the agent
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    payload=payload
)

content = []
for chunk in response.get("response", []):
    content.append(chunk.decode('utf-8'))
print(json.loads(''.join(content)))
