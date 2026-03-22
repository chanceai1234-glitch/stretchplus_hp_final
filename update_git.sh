#!/bin/bash
git reset HEAD~1
echo ".env" >> .gitignore
echo "service-account.json" >> .gitignore
echo "*.pyc" >> .gitignore
git rm --cached .env service-account.json 2>/dev/null
git add .
git commit -m "chore: Final Release - GA4 automation, Claude AI reports, custom favicon, OGP SEO tags, and UI polish"
git push
