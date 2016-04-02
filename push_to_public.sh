#!/bin/bash
# This script is used to push from the internal repository to the public repository.

REPO="https://github.com/MareinK/ru-ai-pacman.git"

echo "Attempting to push public branch to public repository..."
git push $REPO public:master