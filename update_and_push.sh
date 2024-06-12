#!/bin/bash

# Check for unstaged changes
if [[ -n $(git status -s) ]]; then
  # Create a new branch with a timestamp
  BRANCH_NAME="update-$(date +%Y%m%d%H%M%S)"
  git checkout -b $BRANCH_NAME

  # Add all changes
  git add .

  # Commit the changes with a message
  COMMIT_MESSAGE="Update README.md and other changes"
  git commit -m "$COMMIT_MESSAGE"

  # Increase Git buffer size to handle large pushes
  git config --global http.postBuffer 524288000

  # Push the changes to the new branch
  git push origin $BRANCH_NAME

  echo "Changes have been successfully pushed to the repository on branch $BRANCH_NAME."
  echo "Create a Pull Request to merge your changes into the main branch."

  # Switch back to the main branch
  git checkout main

  # Merge the new branch into main
  git merge $BRANCH_NAME

  # Push the changes to the remote main branch
  git push origin main

  echo "Changes have been merged into the main branch and pushed to the remote repository."
else
  # If no changes, push the current branch
  git push
  echo "No changes to commit, but your branch is ahead of 'origin/main'. Pushed local commits to remote."
fi
