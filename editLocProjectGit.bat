@echo off

git fetch origin
git diff main origin/main
git merge origin/main

pause
