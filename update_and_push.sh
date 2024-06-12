#!/bin/bash

# Check for unstaged changes
if [[ -n $(git status -s) ]]; then
  # Create a new branch
  BRANCH_NAME="update-$(date +%Y%m%d%H%M%S)"
  git checkout -b $BRANCH_NAME

  # Add all changes
  git add .

  # Commit the changes with a message
  COMMIT_MESSAGE="Update README.md and other changes"
  git commit -m "$COMMIT_MESSAGE"

  # Push the changes to the new branch
  git push origin $BRANCH_NAME

  echo "Changes have been successfully pushed to the repository on branch $BRANCH_NAME."
  echo "Create a Pull Request to merge your changes into the main branch."
else
  # If no changes, exit with a message
  echo "No changes to commit."
fi