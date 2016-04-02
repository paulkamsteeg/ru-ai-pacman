#!/bin/bash
# This script is used to push from the internal repository to the public repository.

REPO="https://github.com/MareinK/ru-ai-pacman.git"



if [ $(git symbolic-ref --short -q HEAD) = "public" ]
then
  echo "Attempting to push public branch to public repository..."
  git push $REPO public:master
else
  echo "You are not on the public branch."
  echo "You should only push the public branch to the public repository."
  echo "Nothing done."
fi