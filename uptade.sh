#!/bin/bash

# Set your local repository path here
REPO_DIR="$HOME/your-repo-folder"

if [ ! -d "$REPO_DIR" ]; then
  # If the repo doesn't exist locally, clone it
  git clone https://github.com/MaksKostyuk/nOSINT "$REPO_DIR"
else
  # If the repo exists, navigate to it and pull the latest changes
  cd "$REPO_DIR" || exit
  git pull origin main
fi
