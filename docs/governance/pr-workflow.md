# Pull Request Workflow

## Overview

All changes to the curriculum must go through a Pull Request (PR) workflow. This ensures quality, consistency, and proper review.

## Required PR Process

Direct commits to the `main` branch are **not allowed**. Instead:

1. Create a feature branch
2. Make your changes
3. Submit a Pull Request
4. Get approval
5. Merge to main

## Step-by-Step Workflow

### 1. Create a Feature Branch

Start from an up-to-date main branch:

```bash
git checkout main
git pull origin main
git checkout -b feature/description-of-your-change
```

Use descriptive branch names:
- `feature/add-python-module`
- `fix/correct-hours-calculation`
- `docs/update-governance`

### 2. Make Your Changes

Follow the content guidelines:
- Use the standard content structure
- No decorative icons or emojis
- Follow Markdown formatting conventions
- Update `golden_rule_hours.yaml` if hours change

### 3. Validate Locally

Before pushing, validate your changes:

```bash
# Validate Golden Rule hours
python scripts/validate_golden_rule.py

# Test the build
mkdocs build

# Preview locally
mkdocs serve
```

### 4. Commit and Push

```bash
git add .
git commit -m "Brief description of changes"
git push origin feature/description-of-your-change
```

Write clear commit messages:
- Start with a verb (Add, Fix, Update, Remove)
- Keep under 72 characters
- Be specific about what changed

### 5. Create Pull Request

On GitHub:

1. Navigate to the repository
2. Click "Pull Requests" → "New Pull Request"
3. Select your feature branch
4. Fill in the PR template:
   - Title: Brief summary
   - Description: What changed and why
   - Link related issues if applicable

### 6. Automated Checks

The CI pipeline will automatically:

- Validate Golden Rule hours
- Build the documentation
- Generate the PDF
- Check for build errors

All checks must pass before merging.

### 7. Review Process

PRs require approval from at least one reviewer who will check:

- Content accuracy and quality
- Adherence to formatting standards
- Golden Rule compliance
- No decorative icons or emojis in content
- Appropriate documentation updates

### 8. Address Feedback

If reviewers request changes:

```bash
# Make the requested changes
git add .
git commit -m "Address review feedback"
git push origin feature/description-of-your-change
```

The PR will update automatically.

### 9. Merge

Once approved and all checks pass:

1. Squash and merge is recommended for cleaner history
2. Delete the feature branch after merging
3. Pull the updated main branch

```bash
git checkout main
git pull origin main
git branch -d feature/description-of-your-change
```

## PR Best Practices

### Keep PRs Focused

- One logical change per PR
- Smaller PRs are easier to review
- Don't mix unrelated changes

### Write Good Descriptions

A good PR description includes:
- What problem you're solving
- How you solved it
- Any relevant context or decisions
- Screenshots if UI changes

### Respond to Reviews

- Reply to all comments
- Ask questions if feedback is unclear
- Mark conversations as resolved when addressed

### Test Before Submitting

Always validate locally before creating a PR:
- Run the validation script
- Build the documentation
- Review the output

## Protected Branch

The `main` branch has these protections:

- No direct pushes
- Require PR approval
- Require CI checks to pass
- Require up-to-date branch before merge

These protections prevent accidental or unapproved changes.

## Emergency Fixes

For critical issues requiring immediate fixes, the process is the same but can be expedited:

1. Still create a PR (no direct commits)
2. Label as "urgent" or "hotfix"
3. Request immediate review
4. Merge once approved and checks pass

## Questions?

If you're unsure about any part of the workflow, ask in the PR or open an issue for discussion.
