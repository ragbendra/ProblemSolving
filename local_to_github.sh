#!/bin/bash
# local_to_github.sh

# Navigate to the repository
cd /path/to/your/repository || exit

# Add all changes
git add .

# Commit changes with a message
git commit -m "Sync local changes"

# Push changes to GitHub
git push origin main
