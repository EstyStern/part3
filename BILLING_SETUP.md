# Enable Billing for Google Cloud

## Why Billing is Required

Even though Google Cloud has a **free tier**, you need to enable billing to use Cloud Functions and Cloud Run. You won't be charged unless you exceed the free tier limits.

## Free Tier Limits (You're Safe!)

- **Cloud Functions**: 2 million invocations/month FREE
- **Cloud Run**: 2 million requests/month FREE
- **Cloud Build**: 120 build-minutes/day FREE
- **$300 free credit** for 90 days

## Enable Billing

1. Go to: https://console.cloud.google.com/billing?project=aiwordcheckapi
2. Click "Link a billing account"
3. If you don't have one, click "Create billing account"
4. Add a payment method (credit card required, but won't be charged for free tier)
5. Select your billing account and click "Set account"

## After Enabling Billing

1. Wait 1-2 minutes
2. Enable the APIs (see ENABLE_APIS.md)
3. Deploy your function

## Alternative: Use Free Platforms (No Billing Required)

If you prefer not to enable billing, consider these alternatives:

### Option 1: Vercel (Free, No Credit Card)
- Sign up at vercel.com
- Deploy serverless functions
- Free tier available

### Option 2: Railway (Free Tier)
- Sign up at railway.app
- Free tier with $5 credit/month

### Option 3: Render (Free Tier)
- Sign up at render.com
- Free tier available

Would you like me to create a deployment guide for one of these alternatives?

