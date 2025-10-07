#!/usr/bin/env bash
set -euo pipefail
python3 tools/generate_site.py
mkdocs build -d site
echo "Built site in ./site" 
