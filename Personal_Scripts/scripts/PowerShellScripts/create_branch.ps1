# Check if a branch name is provided
if ($args.Count -eq 0) {
    Write-Host "Usage: .\create_branch.ps1 <new-branch-name>"
    exit 1
}

# Prompt the user for the new branch name
$newBranchName = Read-Host "Please enter the new branch name"

# Check if the user provided a branch name
if (-not $newBranchName) {
    Write-Host "Error: No branch name provided. Exiting script."
    exit 1
}

# Fetch all branches from the remote
git fetch

# List all branches, including remote ones
git branch -a

# Create a new branch from the main branch
git checkout main
git pull origin main
# Use the provided branch name to create a new branch
git checkout -b $newBranchName

# Push the new branch to GitHub
git push -u origin $newBranchName

Write-Host "Branch '$newBranchName' created and pushed to GitHub."