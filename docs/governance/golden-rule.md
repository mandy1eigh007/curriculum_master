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

```bash
python scripts/validate_golden_rule.py
```

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
