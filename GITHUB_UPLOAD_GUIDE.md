# GitHub Upload Guide

This guide will walk you through uploading this project to GitHub.

## 📋 Pre-Upload Checklist

✅ All old/duplicate code files removed  
✅ Project structure is clean and organized  
✅ All documentation is complete  
✅ `.gitignore` is configured  
✅ Results and visualization directories are empty (only `.gitkeep` files)

## 🚀 Step-by-Step Upload Process

### Step 1: Initialize Git Repository

Open PowerShell or Command Prompt in the project directory and run:

```bash
cd "C:\Users\群\Desktop\现代投资组合\结课论文"
git init
```

### Step 2: Configure Git (First Time Only)

If you haven't configured Git before:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Add All Files to Git

```bash
git add .
```

This will stage all files according to the `.gitignore` rules.

### Step 4: Create Initial Commit

```bash
git commit -m "Initial commit: Global Asset Portfolio Analysis System v1.0.0

- Modular architecture with clean separation of concerns
- Support for 14 global assets across multiple asset classes
- 7 pre-configured portfolio strategies
- Comprehensive backtesting engine with 11+ performance metrics
- Professional visualization module with 10+ chart types
- Complete English documentation
- Example scripts for quick start
- MIT License"
```

### Step 5: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Sign in** to your account
3. **Click** the "+" icon in the top-right corner
4. **Select** "New repository"

**Repository Settings**:
- **Repository name**: `global-portfolio-analysis`
- **Description**: `A comprehensive framework for global asset portfolio backtesting, optimization, and visualization`
- **Visibility**: Public (recommended for open source)
- **Initialize repository**: 
  - ❌ Do NOT check "Add a README file"
  - ❌ Do NOT add .gitignore
  - ❌ Do NOT choose a license
  
  (We already have these files!)

5. **Click** "Create repository"

### Step 6: Connect Local Repository to GitHub

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/global-portfolio-analysis.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

### Step 7: Verify Upload

1. Refresh your GitHub repository page
2. You should see all files uploaded
3. The README_EN.md will be displayed on the main page

## 🎨 Customize GitHub Repository

### Add Topics (Tags)

1. Click "⚙️ Settings" on your repository
2. Scroll to "Topics"
3. Add these topics:
   - `portfolio-optimization`
   - `backtesting`
   - `finance`
   - `python`
   - `investment`
   - `quantitative-finance`
   - `asset-allocation`
   - `data-science`

### Set Repository Description

In the "About" section (top right), add:
- **Description**: A comprehensive framework for global asset portfolio backtesting, optimization, and visualization
- **Website**: (leave blank or add your website)
- **Topics**: (already added above)

### Enable Features

In Settings → General → Features:
- ✅ Issues (for bug reports and feature requests)
- ✅ Discussions (for community Q&A)
- ✅ Projects (optional)
- ✅ Wiki (optional)

## 📝 Post-Upload Tasks

### 1. Add Repository Badges

Edit `README_EN.md` to add badges at the top (already included):

```markdown
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

### 2. Create a Release

1. Go to "Releases" on the right sidebar
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `Global Asset Portfolio Analysis System v1.0.0`
5. Description: Copy from CHANGELOG.md
6. Click "Publish release"

### 3. Add a GitHub Actions Workflow (Optional)

Create `.github/workflows/python-app.yml` for automated testing:

```yaml
name: Python Application

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 🔄 Updating the Repository

After making changes:

```bash
# Check status
git status

# Add changed files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

## 🌿 Branching Strategy (Optional)

For collaborative development:

```bash
# Create a new branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push branch to GitHub
git push -u origin feature/new-feature

# Create Pull Request on GitHub
# After merge, switch back to main
git checkout main
git pull
```

## 📊 Repository Statistics

After upload, your repository will show:
- **Languages**: Python (primary)
- **Files**: ~20 files
- **Size**: ~50 KB (code only, excluding data)
- **License**: MIT

## 🔗 Share Your Project

Once uploaded, share your repository:

1. **Copy the URL**: `https://github.com/YOUR_USERNAME/global-portfolio-analysis`
2. **Share on**:
   - LinkedIn
   - Twitter
   - Reddit (r/Python, r/algotrading, r/quant)
   - Hacker News
   - Your portfolio website

## 🐛 Troubleshooting

### Issue: "Permission denied (publickey)"

**Solution**: Set up SSH keys or use HTTPS with personal access token.

For HTTPS with token:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/global-portfolio-analysis.git
```

### Issue: "Repository not found"

**Solution**: Check that:
- Repository name is correct
- You're logged in to the correct GitHub account
- Repository is created on GitHub

### Issue: "Failed to push some refs"

**Solution**: Pull first, then push:
```bash
git pull origin main --rebase
git push
```

### Issue: Large files rejected

**Solution**: Our `.gitignore` already excludes large files. If you encounter this:
```bash
# Remove large files from git
git rm --cached path/to/large/file
git commit -m "Remove large file"
git push
```

## 📚 Additional Resources

- [GitHub Docs](https://docs.github.com)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Markdown Guide](https://www.markdownguide.org/)
- [Open Source Guide](https://opensource.guide/)

## ✅ Final Checklist

Before announcing your project:

- [ ] All code is committed and pushed
- [ ] README is clear and comprehensive
- [ ] License is included (MIT)
- [ ] Examples are working
- [ ] Documentation is complete
- [ ] Repository topics are added
- [ ] First release is created
- [ ] Repository description is set

## 🎉 Congratulations!

Your project is now live on GitHub and ready for the world to use!

---

**Next Steps**:
1. Star your own repository (why not? 😄)
2. Share with friends and colleagues
3. Monitor Issues and Pull Requests
4. Keep improving and updating

**Good luck with your open source project!** 🚀
