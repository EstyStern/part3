# AI Text Checker API - Exam Submission

## API Endpoint
**URL:** `https://YOUR_FUNCTION_URL`  
*(Replace with your deployed function URL after deployment)*

## API Description

This is a public cloud API that:
1. Accepts two parameters: `text_to_ai` and `word_to_check`
2. Sends the `text_to_ai` parameter to an AI service
3. Checks if the AI response contains the `word_to_check` parameter
4. Returns the AI response along with the check result

## Request Format

**Method:** POST (or GET with query parameters)

**Content-Type:** application/json

**Request Body:**
```json
{
  "text_to_ai": "Your text to send to AI",
  "word_to_check": "Word to check in response"
}
```

## Response Format

```json
{
  "text_to_ai": "Your text to send to AI",
  "word_to_check": "Word to check in response",
  "ai_response": "The AI's response text...",
  "word_found": true,
  "message": "Word 'Word to check in response' found in AI response"
}
```

## Example Request

```bash
curl -X POST https://YOUR_FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "Explain what is machine learning",
    "word_to_check": "algorithm"
  }'
```

## Example Response

```json
{
  "text_to_ai": "Explain what is machine learning",
  "word_to_check": "algorithm",
  "ai_response": "Machine learning is a subset of AI that uses algorithms...",
  "word_found": true,
  "message": "Word 'algorithm' found in AI response"
}
```

## Public Access

✅ The API is configured to be publicly accessible from anywhere  
✅ CORS is enabled for cross-origin requests  
✅ No authentication required for testing

## Deployment Platform

- **Platform:** Google Cloud Functions (GCP)
- **Runtime:** Python 3.11
- **Region:** us-central1 (configurable)
- **Status:** Public HTTP endpoint

## Testing Instructions

1. Replace `YOUR_FUNCTION_URL` with your actual deployed URL
2. Use the example request above
3. Test from any device or location
4. Verify the response includes the AI response and word check result

## Files Included

- `main.py` - Cloud Function code
- `requirements.txt` - Python dependencies
- `API_DOCUMENTATION.md` - Complete API documentation
- `DEPLOYMENT_STEPS.md` - Step-by-step deployment guide
- `README.md` - General information and usage

---

**Note:** After deployment, update this file with your actual API endpoint URL before submitting.

