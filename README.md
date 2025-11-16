# AI Text Checker Cloud API

This is a Google Cloud Function that sends text to an AI service and checks if the response contains a specific word.

## Features

- Accepts two parameters: `text_to_ai` and `word_to_check`
- Sends text to AI service (OpenAI by default, configurable)
- Checks if AI response contains the specified word
- Returns the AI response with check result
- Public API endpoint (CORS enabled)

## Prerequisites

1. **Google Cloud Account** (Free tier available)
   - Sign up at: https://cloud.google.com/free
   - $300 free credit for 90 days

2. **Google Cloud SDK** (gcloud CLI)
   - Install: https://cloud.google.com/sdk/docs/install

3. **AI API Key** (Optional - for production)
   - OpenAI: https://platform.openai.com/api-keys
   - Or configure for other AI services

## Deployment Steps

### Step 1: Install Google Cloud SDK

```bash
# macOS
brew install google-cloud-sdk

# Or download from: https://cloud.google.com/sdk/docs/install
```

### Step 2: Authenticate with Google Cloud

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### Step 3: Enable Required APIs

```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Step 4: Deploy the Function

```bash
cd cloud-api
gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger=http \
  --allow-unauthenticated \
  --set-env-vars AI_API_KEY=your_api_key_here
```

**Note:** Replace `your_api_key_here` with your actual AI API key, or omit the `--set-env-vars` flag to use mock responses for testing.

### Step 5: Get Your API Endpoint

After deployment, you'll get a URL like:
```
https://us-central1-YOUR_PROJECT_ID.cloudfunctions.net/check-ai-response
```

## API Usage

### Endpoint
```
POST https://YOUR_FUNCTION_URL
```

### Request Body (JSON)
```json
{
  "text_to_ai": "Explain what is machine learning",
  "word_to_check": "algorithm"
}
```

### Query Parameters (Alternative)
```
GET https://YOUR_FUNCTION_URL?text_to_ai=Explain%20AI&word_to_check=algorithm
```

### Response
```json
{
  "text_to_ai": "Explain what is machine learning",
  "word_to_check": "algorithm",
  "ai_response": "Machine learning is a subset of artificial intelligence...",
  "word_found": true,
  "message": "Word 'algorithm' found in AI response"
}
```

## Testing

### Using cURL
```bash
curl -X POST https://YOUR_FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

### Using Python
```python
import requests

url = "https://YOUR_FUNCTION_URL"
data = {
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
}

response = requests.post(url, json=data)
print(response.json())
```

## Configuration

### Environment Variables

- `AI_API_KEY`: Your AI service API key (optional for testing)
- `AI_API_URL`: AI service endpoint (default: OpenAI)
- `AI_MODEL`: AI model to use (default: gpt-3.5-turbo)

### Update Environment Variables
```bash
gcloud functions deploy check-ai-response \
  --update-env-vars AI_API_KEY=your_new_key
```

## Cost

- Google Cloud Functions: Free tier includes 2 million invocations/month
- OpenAI API: Pay-as-you-go (separate cost)
- Total: Essentially free for testing and moderate use

## Troubleshooting

1. **Function not accessible**: Ensure `--allow-unauthenticated` flag is set
2. **CORS errors**: CORS headers are included in the function
3. **AI API errors**: Check your API key and service status
4. **Deployment errors**: Verify you have billing enabled (even with free tier)

## Alternative: Deploy to Other Platforms

### Vercel (Free Tier)
1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json`:
```json
{
  "functions": {
    "api/main.py": {
      "runtime": "python3.9"
    }
  }
}
```
3. Deploy: `vercel --prod`

### Railway (Free Tier)
1. Sign up at railway.app
2. Connect GitHub repository
3. Set environment variables
4. Deploy automatically

