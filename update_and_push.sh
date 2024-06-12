#!/bin/bash

# Change to the directory of your repository (current directory in this case)
REPO_PATH=$(pwd)

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
