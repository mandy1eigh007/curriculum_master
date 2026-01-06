# Governance Overview

This curriculum repository implements comprehensive governance controls to ensure quality, consistency, and integrity of the curriculum content.

## Key Principles

### Single Source of Truth

All curriculum content exists in exactly one location. There are no copies, duplicates, or alternative versions. This ensures:

- Consistency across all uses of the curriculum
- Clear ownership and accountability
- Simplified maintenance and updates
- Prevention of version conflicts

### Immutability of Structure

The Golden Rule hour structure (Core 240 + Math 40 = 280 total) is enforced through automated validation. This ensures curriculum integrity and consistency.

### Change Control

All changes to curriculum content require:

1. Creation of a feature branch
2. Submission of a pull request
3. Review by appropriate stakeholders
4. Automated validation checks
5. Approval before merge

### Protected Master Branch

The main branch is protected to prevent:

- Direct commits
- Unauthorized changes
- Bypassing of review processes
- Validation failures

## Governance Structure

### Content Organization

- **docs/**: All curriculum content in Markdown format
- **curriculum_data/**: Golden Rule configuration and data
- **scripts/**: Validation and automation scripts
- **.github/workflows/**: Automated CI/CD processes

### Validation Mechanisms

1. **Golden Rule Validation**: Automated hour total verification
2. **Build Validation**: Ensures documentation builds successfully
3. **PDF Generation**: Validates export process
4. **Link Checking**: Ensures no broken references

### Release Management

While optional, release tags can be used to mark significant milestones:

- Semantic versioning recommended (v1.0.0, v1.1.0, etc.)
- Tags should reference stable, reviewed content
- Release notes should summarize changes

## Roles and Responsibilities

### Content Authors

- Create and maintain curriculum content
- Follow established templates and formats
- Submit changes via pull requests
- Respond to review feedback

### Reviewers

- Evaluate content for quality and accuracy
- Ensure consistency with curriculum standards
- Verify Golden Rule compliance
- Approve or request changes to pull requests

### Administrators

- Manage repository settings and permissions
- Configure CI/CD workflows
- Maintain governance documentation
- Resolve conflicts and issues

## Compliance

All contributions must comply with:

- Golden Rule hour allocations
- Markdown formatting standards
- ANEW Brand Standard Guidelines
- Single source of truth principle
- No icons or emojis in content

See related pages:

- [Single Source of Truth](single-source.md)
- [Change Control](change-control.md)
- [Golden Rule](golden-rule.md)
