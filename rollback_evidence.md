# Git Rollback Evidence

## Project

Logistic Regression Classification Project

## Purpose

This document demonstrates the use of Git version control and rollback functionality.

## Stable Version

The initial completed project was committed and tagged as:

`v1.0`

Commit message:

`Initial Logistic Regression classification project`

## Rollback Demonstration

A temporary change was made to `README.md` to demonstrate version control.

The temporary change was committed using:

```bash
git add README.md
git commit -m "Add temporary version update for rollback demo"
The temporary commit was then pushed to the remote GitHub repository.
Rollback Command
The project was restored to the stable v1.0 version using:
git reset --hard v1.0
The rollback was then synchronized with GitHub using:
git push --force-with-lease origin main
Verification
The rollback was verified using:
git log --oneline --decorate --all
The main branch returned to the v1.0 commit.
The working tree was also verified using:
git status
The project files remained intact after the rollback.
Result
The rollback successfully restored the project to the stable v1.0 version.
The Git tag v1.0 remains available as a reference to the stable project version.