# Implement docs-as-code curriculum repository with Golden Rule enforcement

## Summary
This PR establishes a docs-as-code curriculum repository for ANEW's pre-apprenticeship program. It includes Golden Rule hour enforcement and a consistent publishing pipeline for web access (and optional PDF export, if enabled).

## Key Changes

### Repository foundation
- MkDocs site configuration and navigation for curriculum content
- Governance docs defining a single source of truth and change control

### Golden Rule enforcement
- Curriculum hour structure defined in `curriculum_data/golden_rule_hours.yaml`
- Validation script `scripts/validate_golden_rule.py` enforcing:
  - Core = 240 hours
  - Math = 40 hours
  - Total = 280 hours
  - Bucket/subunit totals must sum correctly

### Branding and styling
- ANEW brand tokens via CSS (font stack and approved colors)
- Print/PDF stylesheets for consistent exports

### Curriculum content added/updated
- Professional Development module: Grit & Growth Mindset
  - Student-facing page
  - Instructor-facing guide

## Files Modified
- `curriculum_data/golden_rule_hours.yaml`
- `scripts/validate_golden_rule.py`
- `requirements.txt`
- `mkdocs.yml`
- `docs/stylesheets/extra.css`
- `docs/stylesheets/pdf.css`
- `docs/professional-development/grit-growth-mindset/index.md`
- `docs/professional-development/grit-growth-mindset/instructor.md`

## How to test locally
1) Validate Golden Rule totals:
```bash
python scripts/validate_golden_rule.py
```

2) Build documentation site:
```bash
mkdocs build --clean
```

3) Serve locally (optional):
```bash
mkdocs serve
```

## Validation Results
✅ Golden Rule compliance verified  
✅ MkDocs builds successfully  
✅ All merge conflicts resolved  
✅ Repository ready for deployment