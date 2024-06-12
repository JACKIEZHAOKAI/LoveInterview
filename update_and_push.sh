#!/bin/bash

REPO_PATH=$(pwd)

if [[ -n $(git status -s) ]]; then
  git add .
  COMMIT_MESSAGE="Update README.md and other changes"
  git commit -m "$COMMIT_MESSAGE"
  git push origin main
  echo "Changes have been successfully pushed to the repository."
else
  echo "No changes to commit."
fi
