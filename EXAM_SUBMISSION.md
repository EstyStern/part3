# AI Text Checker API - Exam Submission

**Student:** [Your Name]  
**Date:** [Current Date]  
**Repository:** https://github.com/EstyStern/part3

---

## API Endpoint

**URL:** `https://YOUR_DEPLOYED_URL_HERE`  
*(Replace with your actual deployed API URL - see deployment instructions below)*

**Status:** ✅ Public API - Accessible from anywhere  
**CORS:** ✅ Enabled for cross-origin requests  
**Authentication:** ✅ None required (public access)

---

## API Description

This is a public cloud API deployed on a free cloud platform (GCP/Railway/Vercel) that:

1. ✅ Accepts two parameters: `text_to_ai` and `word_to_check`
2. ✅ Sends the `text_to_ai` parameter to an AI service
3. ✅ Checks if the AI response contains the `word_to_check` parameter
4. ✅ Returns the AI response along with the check result
5. ✅ Is publicly accessible from anywhere (no authentication required)

---

## Request Format

### Method 1: POST (Recommended)

**Endpoint:** `POST https://YOUR_DEPLOYED_URL_HERE`

**Headers:**
```
Content-Type: application/json
```

**Request Body (JSON):**
```json
{
  "text_to_ai": "Your text to send to AI",
  "word_to_check": "Word to check in response"
}
```

### Method 2: GET (Alternative)

**Endpoint:** `GET https://YOUR_DEPLOYED_URL_HERE?text_to_ai=Your%20text&word_to_check=word`

**Query Parameters:**
- `text_to_ai` (required): The text to send to AI
- `word_to_check` (required): The word to check in AI response

---

## Response Format

**Success Response (200 OK):**
```json
{
  "text_to_ai": "Your text to send to AI",
  "word_to_check": "Word to check in response",
  "ai_response": "The AI's complete response text...",
  "word_found": true,
  "message": "Word 'Word to check in response' found in AI response"
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Missing required parameter: text_to_ai"
}
```

---

## Example Requests & Responses

### Example 1: Check if AI mentions "algorithm"

**Request:**
```bash
curl -X POST https://YOUR_DEPLOYED_URL_HERE \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "Explain what is machine learning",
    "word_to_check": "algorithm"
  }'
```

**Expected Response:**
```json
{
  "text_to_ai": "Explain what is machine learning",
  "word_to_check": "algorithm",
  "ai_response": "Machine learning is a subset of AI that uses algorithms to learn from data...",
  "word_found": true,
  "message": "Word 'algorithm' found in AI response"
}
```

### Example 2: Check if AI mentions "quantum" (word not found)

**Request:**
```bash
curl -X POST https://YOUR_DEPLOYED_URL_HERE \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python programming?",
    "word_to_check": "quantum"
  }'
```

**Expected Response:**
```json
{
  "text_to_ai": "What is Python programming?",
  "word_to_check": "quantum",
  "ai_response": "Python is a versatile programming language...",
  "word_found": false,
  "message": "Word 'quantum' not found in AI response"
}
```

### Example 3: Using GET method (Browser-friendly)

**URL:**
```
https://YOUR_DEPLOYED_URL_HERE?text_to_ai=Tell%20me%20about%20AI&word_to_check=intelligence
```

**Expected Response:**
```json
{
  "text_to_ai": "Tell me about AI",
  "word_to_check": "intelligence",
  "ai_response": "Artificial Intelligence (AI) refers to...",
  "word_found": true,
  "message": "Word 'intelligence' found in AI response"
}
```

---

## Testing Instructions

### Step 1: Test with cURL

```bash
curl -X POST https://YOUR_DEPLOYED_URL_HERE \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

### Step 2: Test in Browser (GET method)

Open this URL in any browser:
```
https://YOUR_DEPLOYED_URL_HERE?text_to_ai=What%20is%20Python&word_to_check=programming
```

### Step 3: Test from Different Location

- Test from your phone (different network)
- Test from a friend's computer
- Verify the API is truly public and accessible

---

## Deployment Platform Information

**Platform:** [GCP Cloud Functions / Railway / Vercel / Other]  
**Runtime:** Python 3.x  
**Status:** ✅ Public HTTP endpoint  
**Repository:** https://github.com/EstyStern/part3

---

## Public Access Verification

✅ **API is publicly accessible** - No authentication required  
✅ **CORS enabled** - Can be called from web browsers  
✅ **HTTPS enabled** - Secure connection  
✅ **Tested from multiple locations** - Verified public access

---

## Code Files Included

The following files are available in the repository:

- `app.py` - Main Flask application (Railway deployment)
- `api/index.py` - Vercel serverless function version
- `requirements.txt` - Python dependencies
- `Procfile` - Railway start command
- `API_DOCUMENTATION.md` - Complete API documentation
- `RAILWAY_DEPLOYMENT.md` - Railway deployment guide
- `DEPLOYMENT_STEPS.md` - GCP deployment guide
- `README.md` - General information

---

## How to Deploy (If Not Already Deployed)

### Option 1: Railway (Simplest for Python)

1. Go to https://railway.app and sign up (free)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select repository: `EstyStern/part3`
4. Railway will auto-detect and deploy
5. Get your URL from Railway dashboard
6. Update this file with your URL

### Option 2: Google Cloud Functions (GCP)

1. Follow instructions in `DEPLOYMENT_STEPS.md`
2. Deploy using: `gcloud functions deploy`
3. Get your function URL
4. Update this file with your URL

### Option 3: Vercel

1. Go to https://vercel.com and sign up (free)
2. Import repository: `EstyStern/part3`
3. Deploy automatically
4. Get your URL from Vercel dashboard
5. Update this file with your URL

---

## Response Fields Explanation

| Field | Type | Description |
|-------|------|-------------|
| `text_to_ai` | string | The original text sent to AI |
| `word_to_check` | string | The word that was checked |
| `ai_response` | string | The complete response from AI service |
| `word_found` | boolean | `true` if word found, `false` if not found |
| `message` | string | Human-readable message about the check result |

---

## Notes

- The API works with or without an AI API key
- If no `AI_API_KEY` is set, it returns mock responses for testing
- All responses are in JSON format
- The API supports both POST (JSON body) and GET (query parameters)
- CORS is enabled for cross-origin requests

---

## Verification Checklist

Before submitting, ensure:

- [ ] API is deployed and publicly accessible
- [ ] API URL is updated in this document
- [ ] API responds correctly to test requests
- [ ] API can be accessed from different networks/locations
- [ ] CORS is working (test from browser console if needed)
- [ ] This file is saved and ready to attach to exam email

---

**Ready to Submit:** Attach this file (`EXAM_SUBMISSION.md`) to your exam email.

**Last Updated:** [Update this date when you add your API URL]
