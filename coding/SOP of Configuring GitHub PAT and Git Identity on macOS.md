## 1. Creating a Personal Access Token (PAT) on GitHub

1. **Log in to GitHub:**  

. **Access Personal Access Tokens:**  
   Under Developer settings, click **[Personal access tokens](https://github.com/settings/tokens/new)** and then select **Tokens (classic)**.

. **Generate a New Token:**  
   Click **Generate new token**.  
   Select Scopes: For repository access (push/pull, etc.), check at least:
`repo` (for full control of private repositories, if needed)

. **Generate and Copy the Token:**  
   Click **Generate token**. **Immediately copy the token** (you won’t be able to see it again).  
   *Store it securely, for example in a password manager.*

---

2. **PAT Usage:**  
   - When cloning via HTTPS with a PAT, **use your GitHub username** (in this case, `ktwu01`) as the username.  
   - When prompted for a password, **paste your PAT** (the long token you generated on GitHub).  
   This token replaces your GitHub account password in command-line operations.

3. **Configuration on TACC (ls6.tacc):**  
   - On your TACC system, you’ll need to configure Git to use your GitHub identity. For example, run:  
     ```bash
     git config --global user.name "ktwu01"
     git config --global user.email "ktwu01@gmail.com"
     ```

- **A. Verify your Git configuration?**  
  For example, checking that your user name, email, and remote URL are correctly set on TACC. You can run:
  ```bash
  git config --list
  git remote -v
  ```
- **B. Test your authenticated connection to GitHub using your PAT?**  
  For instance, running a command like:
  ```bash
  git ls-remote https://github.com/ktwu01/NOAH-MP-PHS-TACC.git
  ```
  which will query the remote repository without cloning it fully.

- **C. Check your TACC login or environment status?**  
  For example, using:
  ```bash
  whoami
  ```
  to verify your current TACC username.

4. **Credential Storage:**  
   - On your MacBook, you might have configured the macOS Keychain helper to store your credentials. On TACC, check if a similar credential helper is available or if you’ll need to enter your PAT manually each time.


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

