# Deploy to Vercel (Free, No Billing Required!)

Vercel is a free platform that doesn't require billing setup. Perfect for your exam!

## Step 1: Sign Up for Vercel

1. Go to https://vercel.com
2. Click "Sign Up" (use GitHub, GitLab, or email)
3. **No credit card required!**

## Step 2: Install Vercel CLI

```bash
npm install -g vercel
```

Or if you don't have npm:
```bash
brew install vercel-cli
```

## Step 3: Deploy

Navigate to the cloud-api directory and deploy:

```bash
cd "/Users/estern/IdeaProjects/Part 2/cloud-api"
vercel
```

Follow the prompts:
- Set up and deploy? **Yes**
- Which scope? (select your account)
- Link to existing project? **No**
- Project name? (press Enter for default: `cloud-api`)
- Directory? (press Enter for `./`)
- Override settings? **No**

## Step 4: Set Environment Variables (Optional)

If you have an AI API key, set it:

```bash
vercel env add AI_API_KEY
# Paste your API key when prompted
```

Or set it in the Vercel dashboard:
1. Go to your project on vercel.com
2. Settings → Environment Variables
3. Add `AI_API_KEY` with your value

## Step 5: Get Your API URL

After deployment, Vercel will give you a URL like:
```
https://cloud-api-xxxxx.vercel.app/api
```

Your API endpoint will be:
```
https://cloud-api-xxxxx.vercel.app/api
```

## Step 6: Test Your API

```bash
curl -X POST https://YOUR_VERCEL_URL/api \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

## Alternative: Deploy via GitHub

1. Push your code to GitHub
2. Go to vercel.com
3. Click "Add New Project"
4. Import your GitHub repository
5. Vercel will auto-detect and deploy!

## Free Tier Limits

- **100GB bandwidth/month** - FREE
- **100 serverless function executions/day** - FREE
- **Unlimited** for hobby projects
- **No credit card required**

## Update Your Documentation

After deployment, update `API_DOCUMENTATION.md` with your Vercel URL!

