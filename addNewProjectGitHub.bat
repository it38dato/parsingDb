@echo off
set /p repo_url="Enter GitHub repository URL: "
set /p commit_msg="Enter commit message: "

git init
git add .
git commit -m "%commit_msg%"
git branch -M main
git remote add origin %repo_url%
git push -u origin main

pause
