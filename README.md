# Docs website

This repository contains personal documents. This small generator and MkDocs config builds a website and deploys it to GitHub Pages.

Quick start

1. Create a virtualenv and install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Generate site sources and build:

```bash
python tools/generate_site.py
mkdocs build -d site
mkdocs serve
```

3. Deploy: push to GitHub and the included GitHub Actions workflow will build and publish to GitHub Pages.

CI/CD

This repo includes a GitHub Actions workflow that builds the MkDocs site and deploys to the `gh-pages` branch using the official actions.

# docs

Personal manuals and help documents
