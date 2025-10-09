from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel
import boto3

app = BedrockAgentCoreApp()

# Create boto3 session pinned to us-west-2
session = boto3.Session(region_name="us-west-2")

# Create the Bedrock model with both the model_id and session explicitly set
# AWS recently changed how Claude 3.5/4 models (like anthropic.claude-sonnet-4-20250514-v1:0) can be used:
# 👉 These models cannot be invoked directly “on demand” anymore.
# They must be accessed via an Inference Profile, which is like a reserved Bedrock endpoint with guaranteed throughput.
# So we use claude-3-sonnet-20240229-v1:0 which is still supported for on-demand use.
model = BedrockModel(
    boto_session=session,

    # This doesn't work, it tries to use us-east-2
    # model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",

    # This doesn't work, can't use on demand
    # model_id="arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0",

    # Must specify the full ARN to get it to use us-west-2
    model_id="arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",  # on-demand supported
)

print("Using Bedrock region:", model.client.meta.region_name)

# Create the agent
agent = Agent(model=model)

@app.entrypoint
def invoke(payload):
    """Your AI agent function"""
    user_message = payload.get("prompt", "Hello! How can I help you today?")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
