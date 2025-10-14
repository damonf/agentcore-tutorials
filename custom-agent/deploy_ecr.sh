#!/usr/bin/env bash
set -euo pipefail

aws ecr create-repository --repository-name custom-agent --region us-west-2
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 643917810259.dkr.ecr.us-west-2.amazonaws.com
docker buildx build --platform linux/arm64 -t 643917810259.dkr.ecr.us-west-2.amazonaws.com/custom-agent:latest --push .
# verify
aws ecr describe-images --repository-name custom-agent --region us-west-2

