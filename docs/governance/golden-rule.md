<<<<<<< HEAD
# Golden Rule

The Golden Rule defines the immutable hour structure for the curriculum. This structure is enforced through automated validation to prevent drift and ensure curriculum integrity.

## Golden Rule Definition

The curriculum must adhere to the following hour allocations:

- **Core Curriculum (excluding Mathematics):** 240 hours
- **Mathematics:** 40 hours
- **Total:** 280 hours

This structure is **immutable** and cannot be changed without formal approval at the highest governance level.

## Hour Allocation

### Core Curriculum: 240 hours

The core curriculum is divided into:

- **Foundations:** 60 hours
- **Development:** 80 hours
- **Advanced Topics:** 60 hours
- **Capstone:** 40 hours

**Total Core:** 240 hours

### Mathematics: 40 hours

- **Applied Mathematics:** 40 hours

**Total Mathematics:** 40 hours

### Grand Total: 280 hours

Core (240) + Mathematics (40) = **280 hours**

## Configuration Location

The Golden Rule is defined in:

```
curriculum_data/golden_rule_hours.yaml
```

This YAML file contains:

- Hour totals for each bucket
- Subunit breakdowns
- Validation structure

Example structure:

```yaml
core_curriculum:
  hours_total: 240
  subunits:
    - name: "Foundations"
      hours: 60
    - name: "Development"
      hours: 80
    # ...

mathematics:
  hours_total: 40
  subunits:
    - name: "Applied Mathematics"
      hours: 40

total_curriculum:
  hours_total: 280
  components:
    - name: "Core Curriculum"
      hours: 240
    - name: "Mathematics"
      hours: 40
```

## Enforcement Mechanism

### Automated Validation

The Golden Rule is enforced through automated validation:

**Script:** `scripts/validate_golden_rule.py`

This script validates:

1. Each bucket has a `hours_total` field
2. Subunits sum to their bucket's `hours_total`
3. Core curriculum (excluding Math) equals 240 hours
4. Mathematics equals 40 hours
5. Total equals 280 hours

### CI/CD Integration

Validation runs automatically in the CI/CD pipeline:

- Triggered on every pull request
- Must pass before merge is allowed
- Fails the build if validation fails
- Provides clear error messages

### Local Validation

Contributors can validate locally before submitting:
=======
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
>>>>>>> origin/main

```bash
python scripts/validate_golden_rule.py
```

<<<<<<< HEAD
Expected output on success:

```
=== Golden Rule Hours Validation ===

✓ core_curriculum: 240 hours (subunits match total)
✓ mathematics: 40 hours (subunits match total)
✓ total_curriculum: 280 hours (components match total)

✅ Golden Rule validation PASSED: All hour totals are correct!
   - Core (excluding Math): 240 hours
   - Mathematics: 40 hours
   - Total: 280 hours
```

### Validation Failure

If validation fails, the script outputs detailed errors:

```
=== Golden Rule Hours Validation ===

❌ ERROR: core_curriculum subunits sum to 245, but hours_total is 240
❌ Golden Rule validation FAILED: Hour totals do not match requirements
```

## Modifying Hour Allocations

### Within Existing Structure

You **can** modify:

- Distribution within subunits (as long as totals match)
- Content within modules
- Session patterns and delivery methods

You **cannot** modify:

- Total core curriculum hours (must be 240)
- Total mathematics hours (must be 40)
- Grand total hours (must be 280)

### Changing the Golden Rule

The Golden Rule structure is immutable by design. If there is a legitimate need to modify it:

1. Requires executive/governance approval
2. Must document rationale and impact
3. Requires update to governance documentation
4. Must be communicated to all stakeholders
5. Should be rare and exceptional

## Validation Output

### In Pull Requests

The GitHub Actions workflow includes validation as a required check:

- ✅ Green check: Validation passed, PR can be merged
- ❌ Red X: Validation failed, PR blocked

### Build Logs

Validation results appear in build logs:

```
Run python scripts/validate_golden_rule.py
=== Golden Rule Hours Validation ===

✓ core_curriculum: 240 hours (subunits match total)
✓ mathematics: 40 hours (subunits match total)
✓ total_curriculum: 280 hours (components match total)

✅ Golden Rule validation PASSED: All hour totals are correct!
```

## Benefits of Golden Rule Enforcement

### Curriculum Integrity

- Maintains consistent program duration
- Ensures balanced curriculum coverage
- Prevents unintended scope changes
- Supports accreditation requirements

### Quality Assurance

- Automated verification
- Catches errors before merge
- Prevents configuration drift
- Documents hour allocations clearly

### Transparency

- Clear, visible hour structure
- Version-controlled configuration
- Auditable changes
- Stakeholder confidence

## Related Resources

- [Governance Overview](overview.md)
- [Change Control](change-control.md)
- [Single Source of Truth](single-source.md)

## Questions and Support

If you have questions about the Golden Rule:

- Review `curriculum_data/golden_rule_hours.yaml`
- Check validation script output
- Contact curriculum governance team
- Review this documentation
=======
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
>>>>>>> origin/main
