# List all local branches
Write-Host "Current local branches:"
git branch | ForEach-Object { Write-Host $_ }

# Ask for the name of the deleted branch
$deletedBranch = Read-Host "Enter the name of the branch that was deleted on GitHub"

# Check for changes in the current branch
$changes = git status --porcelain
if ($changes) {
    Write-Host "Changes detected in the current branch. Staging changes..."
    git add .

    # Commit the changes with a message
    $commitMessage = "Changes that were made in deleted branch $deletedBranch"
    git commit -m $commitMessage
}

# Switch to a safe branch (e.g., main) before deleting the local branch
git checkout main
git pull origin main

# Apply stashed changes to main if there were any
if ($changes) {
    Write-Host "Applying stashed changes to main..."
    git stash pop
}

# Push the changes to the main branch
if ($changes) {
    Write-Host "Pushing changes to main..."
    git push origin main
}

# Delete the local branch
git branch -d $deletedBranch

# Ask for the name of the new feature branch
$newFeatureBranch = Read-Host "Enter the name of the new feature branch"

# Create and switch to the new feature branch
git checkout -b $newFeatureBranch

Write-Host "Switched to new branch: $newFeatureBranch"