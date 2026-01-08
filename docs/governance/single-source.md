# Single Source of Truth

<<<<<<< HEAD
The curriculum repository operates on the principle that all curriculum content exists in exactly one authoritative location.

## Principle

**One Content, One Location, One Version**

Every piece of curriculum content has a single, canonical representation in this repository. There are no:

- Duplicate files
- Copied sections
- Alternative versions
- Offline copies maintained separately

## Benefits

### Consistency

When content exists in only one place:

- All users access the same information
- Updates are immediately available to everyone
- No confusion about which version is current
- No risk of conflicting information

### Maintainability

Single source of truth simplifies:

- Content updates (change once, apply everywhere)
- Error corrections (fix once, resolved everywhere)
- Review processes (review one authoritative source)
- Version control (clear history of changes)

### Accountability

With a single source:

- Clear ownership of content
- Transparent change history via Git
- Traceable decisions and rationales
- Defined approval processes

## Implementation

### Repository Structure

All content lives in the `docs/` directory:

```
docs/
├── index.md                    # Homepage
├── curriculum/                 # Curriculum content
│   ├── foundations/
│   ├── development/
│   ├── advanced/
│   ├── capstone/
│   └── mathematics/
└── governance/                 # Governance documentation
```

### No External Copies

Content should not be:

- Copied to other repositories
- Duplicated in local documentation
- Maintained in separate systems
- Stored in alternative formats (except generated outputs)

### Generated Outputs

The following are acceptable generated outputs:

- **GitHub Pages site**: Built from Markdown source
- **PDF export**: Generated from Markdown source
- **Local builds**: Temporary for preview purposes

These are not source files and should never be edited directly.

## Workflow

### Making Changes

1. All changes start from the single source in this repository
2. Changes are made via pull requests
3. Reviews ensure quality and accuracy
4. Approved changes are merged to main branch
5. Automated builds update all outputs

### Accessing Content

Users can access content in multiple ways:

- **Web**: Via GitHub Pages (generated from source)
- **PDF**: Via downloaded curriculum.pdf (generated from source)
- **Source**: Directly in repository (authoritative source)

All these views reflect the same underlying content.

## Prohibited Practices

### Do Not:

- Copy content to other locations "for convenience"
- Maintain offline versions that aren't synced
- Create alternative documentation in other tools
- Share outdated snapshots or exports
- Make changes outside the pull request process

### Instead:

- Link to the canonical source
- Use generated outputs for distribution
- Keep all changes in the repository
- Follow the change control process
- Reference specific commits or tags for point-in-time views

## Enforcement

The single source of truth is enforced through:

- **Protected branches**: Prevent unauthorized direct changes
- **Required reviews**: Ensure changes are validated
- **CI/CD automation**: Generate outputs from single source
- **Documentation**: Clear guidance for contributors

## Related Resources

- [Change Control](change-control.md) - How to make changes
- [Governance Overview](overview.md) - Overall governance structure
- [Golden Rule](golden-rule.md) - Hour allocation enforcement
=======
## Principle

This repository is the **single source of truth** for all ANEW curriculum content. There are no copies, no duplicates, and no alternative sources.

## Why This Matters

### Consistency
When content lives in only one place, everyone sees the same information. There's no confusion about which version is current or correct.

### Quality Control
A single source makes it easier to maintain quality standards. Every change goes through the same review process.

### Version History
Git provides complete history of every change. You can see what changed, when it changed, who changed it, and why.

## No Master Copy Drift

Master copy drift occurs when multiple copies of content exist and diverge over time. This creates:

- Confusion about which version is correct
- Wasted effort maintaining multiple sources
- Risk of outdated information being used
- Difficulty tracking changes

### How We Prevent Drift

1. **One Repository**: All content lives in this Git repository
2. **No Copies**: Content is never copied to other systems as editable source
3. **Generated Outputs**: Web and PDF versions are generated from the same Markdown source
4. **Protected Main Branch**: Direct edits to main branch are not allowed

## Content Lifecycle

```
Source Markdown → Build Process → Web + PDF Outputs
     ↓
  (via PR)
     ↓
Protected Main Branch
```

All content changes follow this flow:

1. Edit Markdown files in a feature branch
2. Submit Pull Request
3. Review and approval
4. Merge to main
5. Automated build generates web and PDF

## Consumption, Not Duplication

Other systems may **consume** the curriculum content via:

- Links to the GitHub Pages site
- Downloads of the generated PDF
- API access to the repository (read-only)

Other systems **must not**:

- Copy and edit curriculum content separately
- Maintain their own versions of the curriculum
- Extract and store content without referring back to source

## Enforcement

This principle is enforced through:

- Branch protection rules on main
- Required PR reviews before merge
- Clear documentation and training
- Regular audits for duplicate content
>>>>>>> origin/main
