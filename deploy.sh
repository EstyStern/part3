#!/bin/bash

# AI Text Checker API - Deployment Script
# Run this script from the cloud-api directory

echo "🚀 Deploying AI Text Checker API to Google Cloud Functions..."
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Error: gcloud CLI not found!"
    echo "Please install it first: brew install google-cloud-sdk"
    exit 1
fi

# Get project ID (optional - you can set it manually)
read -p "Enter your GCP Project ID (or press Enter to use current): " PROJECT_ID

if [ ! -z "$PROJECT_ID" ]; then
    echo "Setting project to: $PROJECT_ID"
    gcloud config set project $PROJECT_ID
fi

# Check if AI_API_KEY should be set
read -p "Do you want to set an AI API key? (y/n): " SET_KEY
ENV_VARS=""

if [ "$SET_KEY" = "y" ] || [ "$SET_KEY" = "Y" ]; then
    read -p "Enter your AI API Key: " API_KEY
    ENV_VARS="--set-env-vars AI_API_KEY=$API_KEY"
fi

# Deploy the function
echo ""
echo "📦 Deploying function..."
echo ""

gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger=http \
  --allow-unauthenticated \
  $ENV_VARS

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Your API endpoint will be displayed above."
echo "Look for 'Service URL: https://...' in the output above."
echo ""
echo "To test your API, use:"
echo "curl -X POST YOUR_SERVICE_URL -H 'Content-Type: application/json' -d '{\"text_to_ai\":\"test\",\"word_to_check\":\"test\"}'"

