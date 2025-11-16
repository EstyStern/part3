# Railway Deployment Guide

This guide will help you deploy the AI Text Checker API to Railway, which is simpler and more straightforward than Vercel for Python applications.

## Prerequisites

1. **Railway Account** (Free tier available)
   - Sign up at: https://railway.app
   - Free tier includes $5/month credit

2. **GitHub Account** (for connecting repository)
   - Or use Railway CLI for direct deployment

## Quick Deployment Steps

### Option 1: Deploy via Railway Dashboard (Recommended)

1. **Sign up/Login to Railway**
   - Go to https://railway.app
   - Sign up with GitHub (recommended) or email

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo" (if using GitHub)
   - Or select "Empty Project" to deploy manually

3. **Connect Repository**
   - If using GitHub, select your repository
   - Railway will auto-detect it's a Python project

4. **Configure Deployment**
   - Railway will automatically detect:
     - `requirements.txt` for dependencies
     - `Procfile` for the start command
   - If auto-detection fails, set:
     - **Start Command**: `gunicorn app:app`
     - **Build Command**: (leave empty, Railway handles it)

5. **Set Environment Variables**
   - Go to your project → Variables tab
   - Add the following (optional for testing):
     ```
     AI_API_KEY=your_openai_api_key_here
     AI_API_URL=https://api.openai.com/v1/chat/completions
     AI_MODEL=gpt-3.5-turbo
     ```
   - **Note**: If `AI_API_KEY` is not set, the API will return mock responses for testing

6. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Or click "Deploy" if deploying manually
   - Wait for deployment to complete (usually 1-2 minutes)

7. **Get Your API URL**
   - Once deployed, Railway provides a public URL
   - Example: `https://your-app-name.up.railway.app`
   - You can also set a custom domain in Railway settings

### Option 2: Deploy via Railway CLI

1. **Install Railway CLI**
   ```bash
   npm i -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Project**
   ```bash
   cd cloud-api
   railway init
   ```

4. **Set Environment Variables** (optional)
   ```bash
   railway variables set AI_API_KEY=your_api_key_here
   railway variables set AI_API_URL=https://api.openai.com/v1/chat/completions
   railway variables set AI_MODEL=gpt-3.5-turbo
   ```

5. **Deploy**
   ```bash
   railway up
   ```

6. **Get URL**
   ```bash
   railway domain
   ```

## Project Structure

Railway expects:
- `app.py` - Main Flask application (already created)
- `requirements.txt` - Python dependencies (already exists)
- `Procfile` - Start command (already created)

## API Usage

Once deployed, your API will be available at your Railway URL.

### Endpoint
```
POST https://your-app-name.up.railway.app/
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
GET https://your-app-name.up.railway.app/?text_to_ai=Explain%20AI&word_to_check=algorithm
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
curl -X POST https://your-app-name.up.railway.app/ \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

### Using Python
```python
import requests

url = "https://your-app-name.up.railway.app/"
data = {
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
}

response = requests.post(url, json=data)
print(response.json())
```

## Environment Variables

Set these in Railway dashboard → Variables:

- `AI_API_KEY` (optional): Your OpenAI API key
- `AI_API_URL` (optional): AI service endpoint (default: OpenAI)
- `AI_MODEL` (optional): AI model to use (default: gpt-3.5-turbo)
- `PORT` (automatic): Railway sets this automatically

## Cost

- **Railway Free Tier**: $5/month credit
- **Usage**: ~$0.01 per hour for a small app
- **Total**: Free tier covers light to moderate usage
- **OpenAI API**: Separate cost (pay-as-you-go)

## Advantages of Railway

✅ **Simpler Setup**: No complex configuration files  
✅ **Auto-detection**: Automatically detects Python projects  
✅ **Free Tier**: $5/month credit included  
✅ **Easy Environment Variables**: Set via dashboard  
✅ **Automatic HTTPS**: SSL certificates included  
✅ **Custom Domains**: Easy to add  
✅ **Git Integration**: Auto-deploy on push  

## Troubleshooting

1. **Deployment fails**
   - Check that `requirements.txt` includes all dependencies
   - Verify `Procfile` exists and has correct command
   - Check Railway logs in dashboard

2. **API returns 500 error**
   - Check Railway logs for error details
   - Verify environment variables are set correctly
   - Test locally first: `python app.py`

3. **CORS errors**
   - Flask-CORS is included and should handle CORS automatically
   - If issues persist, check Railway logs

4. **App not responding**
   - Verify the app is running (check Railway dashboard)
   - Check that PORT environment variable is set (Railway sets this automatically)
   - Ensure `gunicorn` is in requirements.txt

## Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Or with gunicorn (production-like)
gunicorn app:app
```

Then test:
```bash
curl -X POST http://localhost:5000/ \
  -H "Content-Type: application/json" \
  -d '{"text_to_ai": "Hello", "word_to_check": "world"}'
```

## Next Steps

1. Deploy to Railway using the steps above
2. Test your API endpoint
3. Update your frontend/client to use the new Railway URL
4. (Optional) Set up a custom domain in Railway settings

