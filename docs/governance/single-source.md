# Single Source of Truth

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
