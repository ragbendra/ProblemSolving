# Path to the main folder containing all your subfolders (Git repository)
$repoPath = "C:\Users\Ragha\Automate"

# Number of files to process per run
$filesToProcessCount = 3

# Navigate to the root of the Git repository
Set-Location -Path $repoPath

# File to track the last processed file
$trackerFile = "$repoPath\last_processed_file.txt"

# Get all .py files that have changes (tracked or untracked) in the repo
$changedFiles = git status --porcelain | Where-Object { $_ -match "\.py" } | ForEach-Object { ($_ -split "\s+")[1] }

# If there are changes, process them
if ($changedFiles.Count -gt 0) {
    # Read last processed file from the tracker
    if (Test-Path $trackerFile) {
        $lastProcessedFile = Get-Content $trackerFile
    }
    else {
        $lastProcessedFile = ""
    }

    # Determine which files to commit (process only the next 2-3 files in sequence)
    $filesToCommit = @()
    $foundLastFile = $false
    
    foreach ($file in $changedFiles) {
        if ($foundLastFile -or $lastProcessedFile -eq "") {
            $filesToCommit += $file
            if ($filesToCommit.Count -ge $filesToProcessCount) { break }
        }
        if ($file -eq $lastProcessedFile) {
            $foundLastFile = $true
        }
    }

    # Commit and push if there are files to commit
    if ($filesToCommit.Count -gt 0) {
        Write-Host "Processing the following files: $($filesToCommit -join ', ')"

        # Stage selected files
        foreach ($file in $filesToCommit) {
            Write-Host "Staging file: $file"
            git add $file
        }

        # Commit and push changes
        $commitMessage = "$(($filesToCommit -join ', ')) on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $commitMessage
        git push origin main  # Replace 'main' with your actual branch name

        # Update the tracker with the last processed file
        $lastProcessedFile = $filesToCommit[-1]  # Update with the last file from the current batch
        $lastProcessedFile | Out-File -FilePath $trackerFile -Encoding UTF8
    }
    else {
        Write-Host "No new files to commit."
    }
}
else {
    Write-Host "No changes detected in the repository. Committing all files."

    # If no changes were detected, commit the rest of the files in the repository
    $allFiles = git ls-files "*.py"
    
    $filesToCommit = @()
    $fileCount = 0

    foreach ($file in $allFiles) {
        $filesToCommit += $file
        $fileCount++
        
        if ($fileCount -ge $filesToProcessCount) {
            # Commit the files in batches of 2-3
            Write-Host "Committing the following files: $($filesToCommit -join ', ')"
            git add $filesToCommit
            $commitMessage = "$(($filesToCommit -join ', ')) on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            git commit -m $commitMessage
            git push origin main  # Replace 'main' with your actual branch name

            # Reset for the next batch of files
            $filesToCommit = @()
            $fileCount = 0
        }
    }

    # If there are remaining files after the loop
    if ($filesToCommit.Count -gt 0) {
        Write-Host "Committing the remaining files: $($filesToCommit -join ', ')"
        git add $filesToCommit
        $commitMessage = "Automated commit for remaining files: $(($filesToCommit -join ', ')) on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $commitMessage
        git push origin main  # Replace 'main' with your actual branch name
    }

    # Update the tracker to ensure no unnecessary commits
    $lastProcessedFile = $allFiles[-1]  # Set last processed file to the last file
    $lastProcessedFile | Out-File -FilePath $trackerFile -Encoding UTF8
}
