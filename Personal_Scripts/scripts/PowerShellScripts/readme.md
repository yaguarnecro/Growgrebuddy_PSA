# Branch Creation Automation Script

This script automates the process of creating a new branch from the `main` branch, fetching all branches, listing them, and pushing the new branch to GitHub.

## Prerequisites

- Ensure you have Git installed on your system.
- You must have access rights to the remote repository on GitHub.
- Make sure you are in the root directory of your Git repository before running the script.
- Use a PowerShell environment on Windows.

## How to Use the Script

1. **Save the Script**: Save the script as `create_branch.ps1`.

2. **Run the Script**: Execute the script with the desired branch name in PowerShell:
   ```powershell
   .\create_branch.ps1 new-branch-name
   ```

   Replace `new-branch-name` with the name of the branch you wish to create.

## What the Script Does

- **Fetches All Branches**: Updates your local repository with all branches from the remote.
- **Lists All Branches**: Displays all local and remote branches.
- **Creates a New Branch**: Creates a new branch from the `main` branch.
- **Pushes the New Branch**: Pushes the newly created branch to the remote repository on GitHub.

## Troubleshooting

- **Permission Denied**: If you encounter a permission error, ensure you have the necessary access rights to the repository.
- **Branch Already Exists**: If the branch name already exists, choose a different name or delete the existing branch if it's no longer needed.

## Additional Information

- This script is intended for use in a Windows environment using PowerShell.
- Ensure your Git configuration is set up correctly to interact with GitHub.

## License

This script is open-source and available under the MIT License. Feel free to modify and distribute it as needed.