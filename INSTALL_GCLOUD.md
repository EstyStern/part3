# Installing Google Cloud SDK - SSL Certificate Fix

The brew installation encountered an SSL certificate issue. Here are alternative installation methods:

## Option 1: Direct Installation (Recommended)

Run this command to install directly from Google:

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

Then add to your PATH (add to ~/.zshrc):
```bash
export PATH=/usr/local/share/google-cloud-sdk/bin:"$PATH"
```

## Option 2: Use Existing Installation

The SDK is already installed at `/usr/local/share/google-cloud-sdk/`. You just need to add it to your PATH.

### Add to PATH permanently:

1. Open your shell config file:
```bash
nano ~/.zshrc
```

2. Add this line at the end:
```bash
export PATH=/usr/local/share/google-cloud-sdk/bin:"$PATH"
```

3. Save and reload:
```bash
source ~/.zshrc
```

4. Verify:
```bash
gcloud --version
```

## Option 3: Fix SSL Certificates

If you still get SSL errors, try:

```bash
# Install certificates
brew install ca-certificates

# Or use Python's certifi
/Applications/Python\ 3.13/Install\ Certificates.command
```

## Option 4: Use Cloud Shell (No Installation Needed)

You can also use Google Cloud Shell directly in your browser:
1. Go to https://console.cloud.google.com
2. Click the Cloud Shell icon (top right)
3. Deploy from there (no local installation needed)

## Quick Test

After adding to PATH, test with:
```bash
gcloud --version
gcloud auth login
```

