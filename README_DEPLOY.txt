QUICK DEPLOYMENT INSTRUCTIONS
==============================

EASIEST METHOD: Use Vercel Web Interface

1. Go to: https://vercel.com
2. Sign up (free, no credit card)
3. Click "Add New Project"
4. Either:
   - Drag & drop this entire "cloud-api" folder, OR
   - Import from GitHub (if you push to GitHub first)

5. Wait 1-2 minutes
6. Get your URL: https://your-project.vercel.app/api

That's it! Your API is live and public!

Test it:
curl -X POST https://YOUR_URL/api \
  -H "Content-Type: application/json" \
  -d '{"text_to_ai":"test","word_to_check":"test"}'
