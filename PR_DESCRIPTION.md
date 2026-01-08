# Implement docs-as-code curriculum repository with Golden Rule enforcement

## Summary
This PR establishes a docs-as-code curriculum repository for ANEW's pre-apprenticeship program. It adds Golden Rule hour enforcement and a MkDocs publishing pipeline for web access. PDF export is included only if the repo's configured exporter/build steps are enabled.

## Key Changes

### Repository foundation
- MkDocs configuration and navigation for curriculum content
- Governance documentation defining single source of truth and change control

### Golden Rule enforcement
- Curriculum hour structure defined in `curriculum_data/golden_rule_hours.yaml`
- Validation script `scripts/validate_golden_rule.py` enforcing:
  - Core = 240 hours
  - Math = 40 hours
  - Total = 280 hours
  - Bucket/subunit totals must sum to declared totals

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
1) Install dependencies:
```bash
pip install -r requirements.txt
```

## Evidence
- Validation + build run locally in Codespace: `python scripts/validate_golden_rule.py` and `mkdocs build --clean`
- CI status: (link to Actions run)
