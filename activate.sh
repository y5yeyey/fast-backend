#!/bin/bash

echo "Creating virtual environment..."

GIT_REPO=`git rev-parse --show-toplevel 2> /dev/null || pwd`

echo "   - configured local git hooks"
git config core.hooksPath hooks

echo "Activate virtual environment: source ./activate.sh"
source "$GIT_REPO/venv/bin/activate"
