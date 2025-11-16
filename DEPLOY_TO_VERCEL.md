# Deploy to Vercel - Web Interface (Easiest Method!)

Since npm has authentication issues, let's use Vercel's web interface - it's actually easier!

## Step 1: Prepare Your Code

Your code is already ready in the `cloud-api` folder with:
- ✅ `api/index.py` - Your serverless function
- ✅ `vercel.json` - Configuration
- ✅ `requirements.txt` - Dependencies (if needed)

## Step 2: Push to GitHub (Recommended)

1. **Create a new GitHub repository:**
   - Go to https://github.com/new
   - Name it: `ai-word-checker-api`
   - Make it **Public** (or Private, both work)
   - Click "Create repository"

2. **Push your code:**
   ```bash
   cd "/Users/estern/IdeaProjects/Part 2/cloud-api"
   git init
   git add .
   git commit -m "Initial commit - AI Word Checker API"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-word-checker-api.git
   git push -u origin main
   ```
   (Replace YOUR_USERNAME with your GitHub username)

## Step 3: Deploy on Vercel

1. **Go to Vercel:**
   - Visit https://vercel.com
   - Click "Sign Up" (use GitHub to sign in - easiest!)

2. **Import Project:**
   - Click "Add New Project"
   - Select "Import Git Repository"
   - Choose your `ai-word-checker-api` repository
   - Click "Import"

3. **Configure:**
   - **Framework Preset:** Other (or leave default)
   - **Root Directory:** `./` (default)
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty)
   - Click "Deploy"

4. **Wait for Deployment:**
   - Takes about 1-2 minutes
   - You'll see build logs
   - When done, you'll get a URL!

## Step 4: Get Your API URL

After deployment, you'll see:
```
✅ Production: https://ai-word-checker-api-xxxxx.vercel.app
```

Your API endpoint will be:
```
https://ai-word-checker-api-xxxxx.vercel.app/api
```

## Step 5: Test Your API

```bash
curl -X POST https://YOUR_VERCEL_URL/api \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

## Alternative: Deploy Without GitHub

If you don't want to use GitHub, you can:

1. **Zip your files:**
   ```bash
   cd "/Users/estern/IdeaProjects/Part 2"
   zip -r cloud-api.zip cloud-api/
   ```

2. **Use Vercel CLI with workaround:**
   - Try: `curl -o- https://cli.vercel.com/install.sh | bash`
   - Or download from: https://vercel.com/download

3. **Or use Vercel's drag-and-drop:**
   - Go to https://vercel.com/new
   - Drag and drop your `cloud-api` folder

## Set Environment Variables (Optional)

If you have an AI API key:

1. Go to your project on Vercel
2. Settings → Environment Variables
3. Add:
   - Name: `AI_API_KEY`
   - Value: `your-api-key-here`
4. Redeploy

## That's It! 🎉

Your API will be live and public, accessible from anywhere!

