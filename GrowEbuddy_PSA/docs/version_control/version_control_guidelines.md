# Version Control Guidelines for GrowEbuddy P.S.A.

## Branching Strategy
- **Main Branch**: The main branch should always be in a deployable state.
- **Feature Branches**: Create a new branch for each feature or bug fix.
  - Naming convention: `feature/feature-name` or `bugfix/issue-name`
- **Release Branches**: Use release branches for preparing production releases.
  - Naming convention: `release/version-number`

## Commit Message Conventions
- **Format**: `<type>(<scope>): <subject>`
  - **Types**: feat, fix, docs, style, refactor, test, chore
  - **Scope**: Optional, but can include the component or module affected
  - **Subject**: Brief description of the change

## Pull Request Process
- **Review**: All pull requests must be reviewed by at least one team member.
- **Testing**: Ensure all tests pass before merging.
- **Merging**: Use squash and merge to maintain a clean commit history.

## Tagging and Releases
- **Tagging**: Use semantic versioning for tags (e.g., v1.0.0).
- **Releases**: Document each release in the changelog.

## Review and Approval
- **Reviewed by**: [DevOps Team Member Names]
- **Approval Date**: [Date] 