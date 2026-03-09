#!/bin/bash

git status

git fetch origin
git diff main origin/main

# Выполнение команд Git
git pull origin main

git diff main origin/main
git status