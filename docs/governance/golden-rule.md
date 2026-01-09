# Golden Rule Enforcement

## The Golden Rule

The ANEW Curriculum follows an immutable "Golden Rule" hour structure:

- **Core Hours** (excluding Mathematics): **240 hours**
- **Mathematics Hours**: **40 hours**
- **Total**: **280 hours**

This structure is **immutable** and must not be violated.

## Why the Golden Rule Exists

### Consistency
A fixed hour structure ensures every student receives the same amount of instruction across all deliveries of the curriculum.

### Quality Assurance
The Golden Rule hours represent a carefully balanced curriculum that covers all necessary topics with appropriate depth.

### Accreditation
Many accreditation bodies and partners require specific hour commitments. The Golden Rule ensures we meet these requirements.

### Resource Planning
Fixed hours enable accurate planning for instructors, facilities, and materials.

## What Can Change

While the total hours are immutable, you can:

- Reorganize content within a bucket
- Adjust subunit hours as long as bucket totals remain the same
- Add or remove topics within the hour constraints
- Change teaching methods or materials
- Update examples and exercises

## What Cannot Change

You **cannot**:

- Change the total to anything other than 280 hours
- Change core hours to anything other than 240
- Change math hours to anything other than 40
- Add hours to one area without removing from another
- Create new top-level categories that would change the core/math split

## Validation System

### Automated Validation

Every Pull Request automatically runs validation:

```bash
python scripts/validate_golden_rule.py
```

This script checks:

1. **Category Totals**: Core = 240, Math = 40
2. **Grand Total**: Sum = 280
3. **Bucket Integrity**: Each bucket's subunits sum to its total
4. **Data Structure**: Proper YAML format and required fields

### When Validation Runs

- Automatically in CI on every PR
- Locally before committing changes
- Before building documentation
- As part of release process

### Validation Failure

If validation fails, the build fails. The PR cannot be merged until:

1. Hours are corrected to meet Golden Rule
2. Validation passes
3. All other checks pass

## Making Hour Changes

If you need to adjust hours within the Golden Rule:

### 1. Update the YAML

Edit `curriculum_data/golden_rule_hours.yaml`:

```yaml
buckets:
  - name: "Your Bucket"
    category: "core"
    hours_total: 80  # Must stay within core total
    subunits:
      - name: "Subunit A"
        hours: 40
      - name: "Subunit B"
        hours: 40  # Must sum to hours_total
```

### 2. Validate Locally

```bash
python scripts/validate_golden_rule.py
```

Fix any errors before committing.

### 3. Update Content

Ensure the Markdown content reflects the new hours:

```markdown
## Required Hours
- **Total Hours**: 40 hours
- **Session Pattern**: 10 sessions of 4 hours
```

### 4. Document the Change

In your PR description, explain:
- Why hours are being redistributed
- What bucket hours changed
- Confirmation that totals remain compliant

## Governance Location

The Golden Rule configuration lives in:

```
curriculum_data/golden_rule_hours.yaml
```

This file defines:
- All curriculum buckets
- Hour allocations
- Subunit breakdowns
- Categories (core vs math)

## Enforcement Mechanisms

### 1. Technical

- Validation script checks every build
- CI fails if validation fails
- Cannot deploy without passing validation

### 2. Process

- PR reviews include hour verification
- Reviewers check Golden Rule compliance
- Documentation updates required for hour changes

### 3. Training

- All contributors learn the Golden Rule
- README documents the requirement
- This page explains enforcement

## Exception Process

There is **no exception process**. The Golden Rule is immutable.

If you believe the Golden Rule itself needs to change, that requires:

1. Organizational decision at the highest level
2. Stakeholder consultation
3. Impact analysis
4. Formal approval process
5. Update to this documentation

This is not a PR-level decision.

## Monitoring and Audits

Regular audits verify:
- Golden Rule compliance in deployed curriculum
- Validation script accuracy
- No circumvention of validation
- Proper categorization of content

## Questions About Hours?

If you're unsure about:
- How to categorize hours
- Whether a change violates Golden Rule
- How to redistribute hours within constraints

Open an issue for discussion before making changes.

## Summary

The Golden Rule is:
- **Immutable**: 240 core + 40 math = 280 total
- **Validated**: Automatically on every build
- **Enforced**: PRs cannot merge if validation fails
- **Clear**: Documented in YAML configuration

When in doubt, run the validation script.
