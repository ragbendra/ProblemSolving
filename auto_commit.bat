@echo off

:: List of repository paths
set REPOS=C:\Users\Ragha\DSA C:\Users\Ragha\LEETCODE C:\Users\Ragha\OOPS

:: Loop through each repository
for %%R in (%REPOS%) do (
    echo Processing %%R
    cd /d %%R

    git add .
    git commit -m "Some Practice Problems"
    git push origin main  :: Replace 'main' with the branch name if it's different
)
