#!/bin/bash


REPO_DIR="$HOME/your-repo-folder"

if [ ! -d "$REPO_DIR" ]; then
  
  git clone https://github.com/MaksKostyuk/nOSINT "$REPO_DIR"
else
 
  cd "$REPO_DIR" || exit
  git pull origin main
fi
