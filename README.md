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

This repo includes GitHub Actions workflows that build the MkDocs site and publish it to either `main/docs` or `gh-pages`, based on your chosen deployment mode.

Publishing changes

If you make a change on the `main` branch and want it published, follow one of these flows depending on your chosen target.

Publish to main/docs (site served from main/docs)

-   Commit and push to `main`:

```bash
git add -A
git commit -m "docs: update content"
git push origin main
```

-   The `deploy.yml` workflow will run on push, build the site, copy built files into `docs/`, and commit them back to `main` (the commit message includes `[skip ci]` to avoid a loop).

Publish to gh-pages (site served from gh-pages branch)

-   Set the repo secret `USE_GHPAGES=true` (Repository → Settings → Secrets and variables → Actions).

-   Commit and push to `main`:

```bash
git add -A
git commit -m "docs: update content"
git push origin main
```

The `deploy-ghpages.yml` workflow will detect `USE_GHPAGES=true`, build the site, and publish the built files to the `gh-pages` branch.

Quick manual publish (if CI is blocked)

If Actions cannot push due to org/repo restrictions, publish manually from your machine.

Publish to `main/docs`:

```bash
python tools/generate_site.py
mkdocs build -d site
rm -rf docs || true
mkdir -p docs
cp -r site/* docs/
git add docs
git commit -m "chore(site): publish site to docs/ [skip ci]"
git push origin main
```

Publish to `gh-pages` (replace branch content):

```bash
python tools/generate_site.py
mkdocs build -d site
git switch gh-pages || git switch -c gh-pages
git rm -rf . || true
cp -r ../site/* .
git add -A
git commit -m "Publish site (manual)"
git push origin gh-pages
git switch main
```

Troubleshooting

-   If Actions cannot push to `gh-pages` or `main`, check Settings → Actions → General → Workflow permissions and ensure "Read and write permissions" is selected for the GITHUB_TOKEN.
-   If pages show 404 after publishing, wait a minute and check the Pages settings for the published URL (Repository → Settings → Pages).
-   If unwanted files (for example `.venv`) got committed to `gh-pages`, remove them in a commit on that branch or replace the branch with a clean publish (see earlier CI/manual steps).

docs

Personal manuals and help documents
