#!/usr/bin/env bash
set -euo pipefail

# Get AWS credentials from the current profile
AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)
AWS_SESSION_TOKEN=$(aws configure get aws_session_token || echo "")
AWS_REGION=$(aws configure get region || echo "us-east-1")

# Check that at least the required ones exist
if [[ -z "$AWS_ACCESS_KEY_ID" || -z "$AWS_SECRET_ACCESS_KEY" ]]; then
  echo "❌ Missing AWS credentials in your profile. Run 'aws configure' first."
  exit 1
fi

echo "✅ Using AWS region: $AWS_REGION"
[[ -n "$AWS_SESSION_TOKEN" ]] && echo "✅ Using temporary credentials" || echo "ℹ️ Using long-lived credentials"

# Run your container
docker run --platform linux/arm64 -p 8080:8080 \
  -e AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID" \
  -e AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" \
  -e AWS_SESSION_TOKEN="$AWS_SESSION_TOKEN" \
  -e AWS_REGION="$AWS_REGION" \
  my-agent:arm64
