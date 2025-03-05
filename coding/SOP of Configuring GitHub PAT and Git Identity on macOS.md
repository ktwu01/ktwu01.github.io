## 1. Creating a Personal Access Token (PAT) on GitHub

1. **Log in to GitHub:**  

. **Access Personal Access Tokens:**  
   Under Developer settings, click **[Personal access tokens](https://github.com/settings/tokens)** and then select **Tokens (classic)**.

. **Generate a New Token:**  
   Click **Generate new token**.  

. **Generate and Copy the Token:**  
   Click **Generate token**. **Immediately copy the token** (you won’t be able to see it again).  
   *Store it securely, for example in a password manager.*

---

## 2. Configuring Git on Your MacBook Terminal

### A. Update Your Git Identity

Set your global Git configuration to use your GitHub name and email:

```bash
git config --global user.name "ktwu01"
git config --global user.email "ktwu01@gmail.com"
```

This ensures all future commits use the correct author details.

### B. Configure Credential Storage

Enable the macOS Keychain helper to securely store your credentials (including your PAT):

```bash
git config --global credential.helper osxkeychain
```

### C. Update Your Remote URL to Use Your GitHub Username

If your repository’s remote URL still uses the old username, update it to include “ktwu01”. For example, run this inside your repository:

```bash
git remote set-url origin https://ktwu01@github.com/kokomomo250/kokomomo250.github.io.git
```

This change tells Git to use “ktwu01” as the username when communicating with GitHub.

### D. Using Your PAT

- **First Push:**  
  When you push changes (e.g., using `git push`), Git will prompt you for a password.  
  - **Enter the PAT** you generated instead of your GitHub account password.
  
- **Storing Credentials:**  
  Because of the credential helper, your PAT will be saved securely in your macOS keychain and used automatically for subsequent operations.

---

## 3. Verifying Everything Works

1. **New Commit Test:**  
   Make a small change, commit, and push:
   ```bash
   git add .
   git commit -m "Test commit using PAT and new identity"
   git push origin main
   ```
   Confirm that the commit appears on GitHub with **ktwu01** as the author.

2. **Remote Verification:**  
   You can also verify that your remote URL is correct by running:
   ```bash
   git remote -v
   ```
   Ensure the URLs include `https://ktwu01@github.com/...`

---

## Additional Questions for Clarity

- **Do you need further details on securing your PAT or managing token expiration?**
- **Would you like guidance on using GitHub’s web interface to revoke or update tokens later on?**
- **Do you have any specific concerns about how these changes might affect your existing repository history or backups?**

Please let me know if any part of this process needs more detail or if you have further questions.
