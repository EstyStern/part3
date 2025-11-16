# Enable Required APIs

Due to SSL certificate issues, please enable these APIs through the web console:

## Required APIs to Enable

1. **Cloud Functions API**
   - https://console.developers.google.com/apis/api/cloudfunctions.googleapis.com/overview?project=aiwordcheckapi
   - Click "ENABLE"

2. **Cloud Build API**
   - https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview?project=aiwordcheckapi
   - Click "ENABLE"

3. **Cloud Run API**
   - https://console.developers.google.com/apis/api/run.googleapis.com/overview?project=aiwordcheckapi
   - Click "ENABLE"

## After Enabling

Wait 1-2 minutes for the APIs to propagate, then run:

```bash
cd "/Users/estern/IdeaProjects/Part 2/cloud-api"
export PATH=/usr/local/share/google-cloud-sdk/bin:"$PATH"
gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger-http \
  --allow-unauthenticated
```

## Alternative: Enable All at Once

You can also enable all APIs at once by visiting:
https://console.cloud.google.com/apis/library?project=aiwordcheckapi

Then search for and enable:
- Cloud Functions API
- Cloud Build API  
- Cloud Run API

