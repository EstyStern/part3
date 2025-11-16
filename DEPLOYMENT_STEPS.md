# Step-by-Step Deployment Guide

Follow these steps to deploy your AI Text Checker API to Google Cloud Platform.

## Step 1: Create Google Cloud Account

1. Go to https://cloud.google.com/free
2. Click "Get started for free"
3. Sign up with your Google account
4. Complete the registration (credit card may be required but won't be charged for free tier usage)

## Step 2: Create a New Project

1. Go to https://console.cloud.google.com
2. Click on the project dropdown at the top
3. Click "New Project"
4. Enter project name: `ai-text-checker` (or any name you prefer)
5. Click "Create"
6. Wait for project creation (takes a few seconds)

## Step 3: Install Google Cloud SDK

### macOS:
```bash
brew install google-cloud-sdk
```

### Windows:
Download and install from: https://cloud.google.com/sdk/docs/install

### Linux:
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

## Step 4: Authenticate and Configure

1. Open terminal/command prompt
2. Run:
```bash
gcloud auth login
```
3. This will open a browser - sign in with your Google account
4. Set your project:
```bash
gcloud config set project YOUR_PROJECT_ID
```
   (Replace YOUR_PROJECT_ID with your actual project ID from Step 2)

## Step 5: Enable Required APIs

Run these commands:
```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
```

## Step 6: Get AI API Key (Optional for Testing)

### Option A: Use OpenAI (Recommended)
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy the key (you'll need it in Step 7)

### Option B: Skip for Testing
- The function will use mock responses if no API key is provided
- Good for initial testing

## Step 7: Deploy the Function

1. Navigate to the cloud-api directory:
```bash
cd "/Users/estern/IdeaProjects/Part 2/cloud-api"
```

2. Deploy the function:

**With AI API Key:**
```bash
gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger=http \
  --allow-unauthenticated \
  --set-env-vars AI_API_KEY=your_openai_api_key_here
```

**Without AI API Key (for testing):**
```bash
gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger=http \
  --allow-unauthenticated
```

3. Wait for deployment (takes 2-5 minutes)
4. You'll see output like:
```
Service URL: https://check-ai-response-xxxxx-uc.a.run.app
```

## Step 8: Test Your API

1. Copy the Service URL from Step 7
2. Test with cURL:
```bash
curl -X POST https://YOUR_SERVICE_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

3. Or test in browser (GET method):
```
https://YOUR_SERVICE_URL?text_to_ai=What%20is%20Python&word_to_check=programming
```

## Step 9: Verify Public Access

1. Open the Service URL in a browser
2. You should see an error (expected - needs parameters)
3. Try with parameters in the URL
4. Test from a different device/network to confirm it's public

## Step 10: Document Your API Endpoint

1. Open `API_DOCUMENTATION.md`
2. Replace `YOUR_FUNCTION_URL` with your actual Service URL
3. Save the file
4. This file is ready to attach to your exam email

## Troubleshooting

### Error: "Permission denied"
- Make sure billing is enabled (even for free tier)
- Go to: https://console.cloud.google.com/billing
- Link a billing account to your project

### Error: "API not enabled"
- Run the enable commands from Step 5 again

### Error: "Function not found"
- Make sure you're in the correct directory
- Check that main.py and requirements.txt exist

### Function not accessible
- Verify `--allow-unauthenticated` flag was used
- Check function permissions in Cloud Console

### CORS errors
- CORS is already configured in the code
- Make sure you're using the correct URL

## Next Steps

1. ✅ API is deployed and public
2. ✅ Test from multiple locations
3. ✅ Document your endpoint URL
4. ✅ Attach API_DOCUMENTATION.md to your exam email

## Cost Estimate

- **Free Tier**: 2 million invocations/month
- **Storage**: Minimal (free tier covers it)
- **AI API**: Separate cost (OpenAI charges per request)
- **Total**: Essentially free for testing and moderate use

---

**Your API is now live and accessible from anywhere!** 🌐

