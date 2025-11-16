# Quick Start Guide - Where to Run Commands

## 📍 Command Locations

### Step 1: Install Google Cloud SDK
**Run from: ANYWHERE (your home directory, desktop, anywhere)**

```bash
brew install google-cloud-sdk
```

This installs software on your Mac, so location doesn't matter.

---

### Step 2: Authenticate with Google Cloud
**Run from: ANYWHERE**

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

---

### Step 3: Navigate to Project Directory
**Run from: Terminal (anywhere first, then navigate)**

```bash
cd "/Users/estern/IdeaProjects/Part 2/cloud-api"
```

**OR use the full path:**
```bash
cd ~/IdeaProjects/Part\ 2/cloud-api
```

---

### Step 4: Deploy the Function
**Run from: `/Users/estern/IdeaProjects/Part 2/cloud-api` directory**

**Option A: Use the deployment script (easiest)**
```bash
./deploy.sh
```

**Option B: Manual deployment**
```bash
gcloud functions deploy check-ai-response \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=check_ai_response \
  --trigger=http \
  --allow-unauthenticated
```

---

## 📂 Directory Structure

```
Part 2/
└── cloud-api/          ← Run deployment commands from HERE
    ├── main.py
    ├── requirements.txt
    ├── deploy.sh       ← Or run this script
    └── ...
```

---

## ✅ Quick Checklist

- [ ] Install gcloud: `brew install google-cloud-sdk` (from anywhere)
- [ ] Authenticate: `gcloud auth login` (from anywhere)
- [ ] Navigate: `cd "/Users/estern/IdeaProjects/Part 2/cloud-api"`
- [ ] Deploy: `./deploy.sh` or use gcloud command (from cloud-api directory)

---

## 🎯 Summary

- **Installation commands**: Run from anywhere
- **Deployment commands**: Must run from `cloud-api` directory
- **Why?**: The `--source=.` flag tells gcloud to use files in the current directory

