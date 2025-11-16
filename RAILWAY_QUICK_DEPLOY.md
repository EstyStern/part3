# 🚂 Railway Quick Deploy Guide

## Step-by-Step Deployment

### Step 1: Sign Up for Railway
1. Go to **https://railway.app**
2. Click **"Start a New Project"** or **"Login"**
3. Sign up with **GitHub** (recommended - easiest)
   - Or use email if you prefer
4. **No credit card required!** Free tier includes $5/month

### Step 2: Create New Project
1. After logging in, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your GitHub (if needed)

### Step 3: Select Your Repository
1. Find and select: **`EstyStern/part3`**
2. Click on it
3. Railway will start deploying automatically

### Step 4: Configure Deployment (Auto-detected)
Railway will automatically detect:
- ✅ Python project (from `requirements.txt`)
- ✅ Start command (from `Procfile`: `gunicorn app:app`)
- ✅ Dependencies (from `requirements.txt`)

**You don't need to change anything!** Just wait for deployment.

### Step 5: Get Your API URL
1. Wait 1-2 minutes for deployment to complete
2. Once deployed, Railway will show you a URL like:
   ```
   https://your-app-name.up.railway.app
   ```
3. Click on the service → **Settings** → **Generate Domain**
4. Copy your public URL

### Step 6: Test Your API
Test with this command (replace with your URL):
```bash
curl -X POST https://YOUR_RAILWAY_URL \
  -H "Content-Type: application/json" \
  -d '{
    "text_to_ai": "What is Python?",
    "word_to_check": "programming"
  }'
```

Or test in browser:
```
https://YOUR_RAILWAY_URL?text_to_ai=Hello&word_to_check=world
```

### Step 7: Set Environment Variables (Optional)
If you want real AI responses (not mock):
1. Go to your project → **Variables** tab
2. Add:
   - `AI_API_KEY` = your OpenAI API key (optional)
   - `AI_API_URL` = https://api.openai.com/v1/chat/completions (optional)
   - `AI_MODEL` = gpt-3.5-turbo (optional)

**Note:** Without `AI_API_KEY`, the API will return mock responses (still works for testing!)

### Step 8: Update EXAM_SUBMISSION.md
1. Open `EXAM_SUBMISSION.md`
2. Find: `https://YOUR_DEPLOYED_URL_HERE`
3. Replace with: `https://YOUR_RAILWAY_URL`
4. Save the file
5. Commit and push:
   ```bash
   git add EXAM_SUBMISSION.md
   git commit -m "Update API URL for exam submission"
   git push origin main
   ```

---

## Troubleshooting

### Deployment Fails?
- Check Railway logs (click on your service → Logs)
- Verify `requirements.txt` has all dependencies
- Make sure `Procfile` exists and has: `web: gunicorn app:app`

### API Not Responding?
- Check Railway logs for errors
- Verify the service is running (green status)
- Test with the curl command above

### Need Help?
- Railway logs show all errors
- Check that `app.py` is in the root directory
- Verify `Procfile` is in the root directory

---

## ✅ Success Checklist

- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] Deployment completed successfully
- [ ] Got your Railway URL
- [ ] Tested API with curl or browser
- [ ] Updated `EXAM_SUBMISSION.md` with your URL
- [ ] API is publicly accessible

---

## 🎉 You're Done!

Once deployed, your API will be:
- ✅ Publicly accessible from anywhere
- ✅ Free (within Railway's free tier)
- ✅ Ready for your exam!

**Your API URL format:**
```
https://your-app-name.up.railway.app
```

Use this URL in your `EXAM_SUBMISSION.md` file!

