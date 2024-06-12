#!/bin/bash

# Change to the directory of your repository
cd /path/to/your/repository

# Check for unstaged changes
if [[ -n $(git status -s) ]]; then
  # Add all changes
  git add .

  # Commit the changes with a message
  git commit -m "Update README.md and other changes"

  # Push the changes to the remote repository
  git push origin main

  echo "Changes have been successfully pushed to the repository."
else
  echo "No changes to commit."
fi
