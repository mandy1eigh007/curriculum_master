# ANEW Curriculum - Docs-as-Code

A comprehensive curriculum repository implementing "docs-as-code" principles with automated validation, PDF generation, and GitHub Pages deployment.

## Overview

This repository contains the ANEW curriculum optimized for the immutable "Golden Rule" hour structure:

- **Core Curriculum (excluding Mathematics):** 240 hours
- **Mathematics:** 40 hours
- **Total:** 280 hours

## Features

- **Docs-as-Code**: All curriculum content in Markdown format
- **Golden Rule Enforcement**: Automated validation of hour totals in CI/CD
- **PDF Generation**: Automatic aggregated PDF export via mkdocs-exporter
- **GitHub Pages**: Public access via automatically deployed static site
- **Protected Branch**: Governance controls prevent master-copy drift
- **ANEW Brand Standards**: Professional styling following brand guidelines
- **Single Source of Truth**: No duplicate content, all in one location

## Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository:**

```bash
git clone https://github.com/mandy1eigh007/curriculum_master.git
cd curriculum_master
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Install Playwright (required for PDF generation):**

```bash
playwright install chromium
```

4. **Serve locally with live reload:**

```bash
mkdocs serve
```

Visit `http://localhost:8000` to preview the documentation.

5. **Build static site:**

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## PDF Generation

PDF is automatically generated during the build process using the mkdocs-exporter plugin.

### Manual PDF Generation

```bash
mkdocs build
```

The aggregated PDF will be output to: `site/downloads/curriculum.pdf`

### PDF Features

- **Aggregated Output**: Single PDF containing all curriculum content
- **ANEW Brand Styling**: Professional formatting with brand colors and fonts
- **Page Breaks**: Automatic section separation
- **Headers/Footers**: Title and page numbers on each page
- **Clean Design**: No decorative icons, professional appearance

## Repository Structure

```
curriculum_master/
├── .github/
│   └── workflows/
│       └── pages.yml              # GitHub Actions workflow for deployment
├── curriculum_data/
│   └── golden_rule_hours.yaml     # Golden Rule hour configuration
├── docs/
│   ├── curriculum/                # Curriculum content
│   │   ├── foundations/
│   │   ├── development/
│   │   ├── advanced/
│   │   ├── capstone/
│   │   └── mathematics/
│   ├── governance/                # Governance documentation
│   ├── stylesheets/
│   │   ├── extra.css             # Web styling
│   │   └── pdf.css               # PDF-specific styling
│   └── index.md                  # Homepage
├── scripts/
│   └── validate_golden_rule.py   # Golden Rule validation script
├── .gitignore
├── CHANGELOG.md
├── mkdocs.yml                     # MkDocs configuration
├── README.md
└── requirements.txt               # Python dependencies
```

## Adding Content

### Content Structure

All curriculum content must include the following sections:

1. **Required Hours**: Specify hour allocation
2. **Session Pattern**: Breakdown of time by activity type
3. **Purpose**: Module objectives and goals
4. **Learning Outcomes**: What students will be able to do
5. **Core Content**: Main curriculum material
6. **Deliverables**: Expected outputs and assessments

### Creating New Content

1. Create a new Markdown file in the appropriate `docs/curriculum/` subdirectory
2. Follow the existing content template structure
3. Update `mkdocs.yml` navigation to include the new page
4. Test locally before submitting

### Formatting Guidelines

- Use standard Markdown syntax
- No icons or emojis in content (site UI icons are acceptable)
- Follow ANEW Brand Standards for styling
- Use clear, professional language
- Include proper heading hierarchy (H1 → H2 → H3)

## Change Control

All changes must follow the pull request workflow:

1. **Create a feature branch:**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** following content guidelines

3. **Validate locally:**

```bash
# Validate Golden Rule hours
python scripts/validate_golden_rule.py

# Test build
mkdocs build
```

4. **Commit and push:**

```bash
git add .
git commit -m "Descriptive commit message"
git push origin feature/your-feature-name
```

5. **Create pull request** on GitHub

6. **Wait for automated checks** to pass:
   - Golden Rule validation
   - Build verification
   - PDF generation

7. **Get approval** from reviewers

8. **Merge** once approved and all checks pass

See [Change Control Documentation](docs/governance/change-control.md) for complete details.

## Golden Rule Validation

The Golden Rule hour structure is enforced through automated validation.

### Location

- **Configuration**: `curriculum_data/golden_rule_hours.yaml`
- **Validation Script**: `scripts/validate_golden_rule.py`

### Running Validation

```bash
python scripts/validate_golden_rule.py
```

### Validation Rules

The script validates:

- Core curriculum totals 240 hours
- Mathematics totals 40 hours
- Grand total equals 280 hours
- All subunits sum to their bucket totals
- All required fields are present

### CI/CD Integration

Validation runs automatically on every pull request and must pass before merge is allowed.

See [Golden Rule Documentation](docs/governance/golden-rule.md) for complete details.

## Governance

This repository implements strict governance controls:

- **Single Source of Truth**: All content in one location, no duplicates
- **Protected Branch**: Main branch requires PR approval
- **Required Reviews**: Changes must be reviewed before merge
- **Automated Validation**: Golden Rule and build checks must pass
- **No Master-Copy Drift**: Governance prevents divergence

See the [Governance Documentation](docs/governance/overview.md) for complete details.

## Brand Standards

This repository follows ANEW Brand Standard Guidelines:

### Typography

- **Primary Typeface**: Helvetica Neue, Helvetica, Arial, sans-serif

### Colors

- **Blue**: #326691 (Primary)
- **Green**: #3FAE49 (Accent)
- **Gray**: #505858 (Text)

### Styling

- Defined in `docs/stylesheets/extra.css` (web)
- Defined in `docs/stylesheets/pdf.css` (PDF)
- CSS variables for consistency
- Clean, professional, non-decorative design

## Public Access

The curriculum is publicly accessible via:

- **GitHub Pages**: https://mandy1eigh007.github.io/curriculum_master/
- **PDF Download**: Available from the homepage
- **Source Repository**: https://github.com/mandy1eigh007/curriculum_master

## Deployment

### Automatic Deployment

GitHub Actions automatically deploys to GitHub Pages when changes are pushed to the main branch.

### Workflow

1. Code is pushed to main branch
2. GitHub Actions workflow triggers
3. Dependencies are installed
4. Golden Rule validation runs
5. MkDocs builds the site and PDF
6. Site is deployed to GitHub Pages

### Manual Deployment

If needed, deployment can be triggered manually via the Actions tab in GitHub.

## Contributing

Contributions are welcome! Please:

1. Review governance documentation
2. Follow content and formatting guidelines
3. Test changes locally before submitting
4. Create pull requests for all changes
5. Respond to review feedback

## License

This curriculum is maintained by ANEW.

## Support

For questions or issues:

- Review documentation in `docs/governance/`
- Check existing issues on GitHub
- Create a new issue for bugs or questions
- Contact repository administrators

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes.

## Acknowledgments

- Built with [MkDocs](https://www.mkdocs.org/)
- Theme: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- PDF Export: [mkdocs-exporter](https://github.com/adrienbrault/mkdocs-exporter)