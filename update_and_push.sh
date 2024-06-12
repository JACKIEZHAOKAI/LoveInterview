#!/bin/bash

# Define the repository path
REPO_PATH="."

# Change to the directory of your repository
cd $REPO_PATH || { echo "Repository path not found"; exit 1; }

# Check for unstaged changes
if [[ -n $(git status -s) ]]; then
  # Add all changes
  git add .

  # Commit the changes with a message
  COMMIT_MESSAGE="Update README.md and other changes"
  git commit -m "$COMMIT_MESSAGE"

  # Push the changes to the remote repository
  git push origin main

  echo "Changes have been successfully pushed to the repository."
else
  echo "No changes to commit."
fi
