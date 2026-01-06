# Change Control

All changes to curriculum content follow a structured change control process to ensure quality, consistency, and proper review.

## Change Control Process

### 1. Create Feature Branch

Start by creating a branch for your changes:

```bash
git checkout -b feature/descriptive-name
```

Branch naming conventions:

- `feature/` - New content or functionality
- `fix/` - Bug fixes or corrections
- `docs/` - Documentation updates
- `update/` - Content updates or revisions

### 2. Make Changes

Edit content following established standards:

- Use Markdown format
- Follow content templates
- No icons or emojis in content
- Apply ANEW Brand Standards
- Maintain Golden Rule hour allocations

### 3. Test Locally

Before submitting, test your changes:

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Validate Golden Rule hours
python scripts/validate_golden_rule.py

# Build and preview
mkdocs serve
```

Visit `http://localhost:8000` to preview changes.

### 4. Commit Changes

Commit your changes with clear messages:

```bash
git add .
git commit -m "Descriptive commit message"
```

Commit message guidelines:

- Use present tense ("Add feature" not "Added feature")
- Be specific and descriptive
- Reference issues if applicable
- Keep first line under 50 characters
- Add detailed description if needed

### 5. Push Branch

Push your branch to the repository:

```bash
git push origin feature/descriptive-name
```

### 6. Create Pull Request

Create a pull request on GitHub:

1. Navigate to the repository
2. Click "Pull requests" → "New pull request"
3. Select your branch
4. Fill in title and description
5. Request reviewers
6. Submit pull request

### 7. Automated Checks

The CI/CD pipeline will automatically:

- Validate Golden Rule hour totals
- Build the documentation
- Generate PDF export
- Check for errors

All checks must pass before merge is allowed.

### 8. Review Process

Reviewers will:

- Evaluate content quality and accuracy
- Check formatting and consistency
- Verify Golden Rule compliance
- Test builds locally if needed
- Provide feedback or approval

### 9. Address Feedback

If changes are requested:

1. Make requested modifications
2. Commit and push updates
3. Respond to reviewer comments
4. Request re-review if needed

### 10. Merge

Once approved and all checks pass:

- Reviewer or admin merges pull request
- Branch is deleted after merge
- Main branch is updated
- GitHub Pages automatically redeploys

## Review Standards

### Content Quality

- Accurate and current information
- Clear and professional writing
- Appropriate depth and detail
- Logical organization

### Format Compliance

- Valid Markdown syntax
- Consistent formatting
- No decorative icons/emojis
- Proper heading hierarchy

### Structural Requirements

- Required sections present
- Hour allocations specified
- Learning outcomes defined
- Deliverables documented

### Golden Rule Compliance

- Hour totals must validate
- Cannot modify Golden Rule structure
- Must maintain 280 total hours
- Core and Math separation preserved

## Release Tagging (Optional)

For significant milestones, create release tags:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Release tags should:

- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Include release notes
- Mark stable, reviewed content
- Reference significant changes

## Emergency Procedures

For critical issues requiring immediate attention:

1. Follow standard process when possible
2. Mark PR as "urgent" in title
3. Request expedited review
4. Document reason for urgency
5. Still require approval before merge

**Note**: Even emergencies require review. Direct commits to main are not allowed.

## Getting Help

If you need assistance:

- Review this documentation
- Check existing pull requests for examples
- Ask in pull request comments
- Contact repository administrators

## Related Resources

- [Governance Overview](overview.md)
- [Single Source of Truth](single-source.md)
- [Golden Rule](golden-rule.md)
