# AI Text Checker API - Documentation

## API Endpoint Information

**Base URL:** `https://YOUR_FUNCTION_URL`  
*(Replace with your actual deployed function URL)*

**Status:** Public API - Accessible from anywhere

---

## Endpoint Details

### POST / (or GET with query parameters)

Sends text to an AI service and checks if the response contains a specific word.

### Request

#### Method: POST (Recommended)

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "text_to_ai": "string (required) - The text to send to AI",
  "word_to_check": "string (required) - The word to check in AI response"
}
```

#### Method: GET (Alternative)

**Query Parameters:**
- `text_to_ai` (required): The text to send to AI
- `word_to_check` (required): The word to check in AI response

**Example:**
```
GET /?text_to_ai=What%20is%20Python&word_to_check=programming
```

### Response

**Success Response (200 OK):**
```json
{
  "text_to_ai": "What is Python?",
  "word_to_check": "programming",
  "ai_response": "Python is a high-level programming language...",
  "word_found": true,
  "message": "Word 'programming' found in AI response"
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Missing required parameter: text_to_ai"
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "error": "Error message here",
  "message": "An error occurred while processing the request"
}
```

---

## Example Requests

### Example 1: Check if AI mentions "algorithm"

**Request:**
```bash
curl -X POST https://YOUR_FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "Explain machine learning",
    "word_to_check": "algorithm"
  }'
```

**Response:**
```json
{
  "text_to_ai": "Explain machine learning",
  "word_to_check": "algorithm",
  "ai_response": "Machine learning uses algorithms to learn from data...",
  "word_found": true,
  "message": "Word 'algorithm' found in AI response"
}
```

### Example 2: Check if AI mentions "quantum"

**Request:**
```bash
curl -X POST https://YOUR_FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python programming?",
    "word_to_check": "quantum"
  }'
```

**Response:**
```json
{
  "text_to_ai": "What is Python programming?",
  "word_to_check": "quantum",
  "ai_response": "Python is a versatile programming language...",
  "word_found": false,
  "message": "Word 'quantum' not found in AI response"
}
```

### Example 3: Using GET method

**Request:**
```
GET https://YOUR_FUNCTION_URL?text_to_ai=Tell%20me%20about%20AI&word_to_check=intelligence
```

**Response:**
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

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `text_to_ai` | string | The original text sent to AI |
| `word_to_check` | string | The word that was checked |
| `ai_response` | string | The complete response from AI |
| `word_found` | boolean | Whether the word was found in AI response |
| `message` | string | Human-readable message about the check result |

---

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS), allowing it to be called from web browsers and any other client.

**CORS Headers:**
- `Access-Control-Allow-Origin: *`
- `Access-Control-Allow-Methods: GET, POST, OPTIONS`
- `Access-Control-Allow-Headers: Content-Type`

---

## Testing the API

### Using cURL
```bash
curl -X POST https://YOUR_FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is artificial intelligence?",
    "word_to_check": "machine"
  }'
```

### Using Python
```python
import requests

url = "https://YOUR_FUNCTION_URL"
payload = {
    "text_to_ai": "What is artificial intelligence?",
    "word_to_check": "machine"
}

response = requests.post(url, json=payload)
print(response.json())
```

### Using JavaScript (Fetch)
```javascript
fetch('https://YOUR_FUNCTION_URL', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text_to_ai: 'What is artificial intelligence?',
    word_to_check: 'machine'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Using Postman
1. Method: POST
2. URL: `https://YOUR_FUNCTION_URL`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
  "text_to_ai": "What is artificial intelligence?",
  "word_to_check": "machine"
}
```

---

## Error Handling

The API returns appropriate HTTP status codes:

- **200 OK**: Request successful
- **400 Bad Request**: Missing or invalid parameters
- **500 Internal Server Error**: Server error or AI service error

All error responses include an `error` field with details.

---

## Rate Limits

Rate limits depend on your cloud provider:
- **Google Cloud Functions**: 2 million invocations/month (free tier)
- Additional usage may incur charges

---

## Security Notes

- The API is public and does not require authentication
- For production use, consider adding API key authentication
- AI API keys should be stored as environment variables (not in code)

---

## Support

For issues or questions:
1. Check the deployment logs in Google Cloud Console
2. Verify your AI API key is correctly configured
3. Ensure the function is deployed with `--allow-unauthenticated` flag

---

**Last Updated:** [Current Date]  
**API Version:** 1.0  
**Status:** Public and Active

