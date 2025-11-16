# Push to GitHub - Quick Steps

## Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. Repository name: `Part-3-` (or any name you prefer)
3. Description: "AI Word Checker API"
4. Choose: **Public** or **Private**
5. **DO NOT** check "Add a README file"
6. **DO NOT** add .gitignore or license
7. Click **"Create repository"**

## Step 2: Push Your Code

After creating the repo, run these commands:

```bash
cd "/Users/estern/IdeaProjects/Part 2/cloud-api"

# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Part-3-.git

# Push to GitHub
git push -u origin main
```

Or if you use SSH:
```bash
git remote add origin git@github.com:YOUR_USERNAME/Part-3-.git
git push -u origin main
```

## Step 3: Deploy on Vercel

1. Go back to Vercel
2. Click **"Continue with GitHub"**
3. Select your `Part-3-` repository
4. Click **"Import"**
5. Wait for deployment!

That's it! 🚀


