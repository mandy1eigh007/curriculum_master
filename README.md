# ANEW Curriculum Master

A comprehensive curriculum repository implementing "docs-as-code" principles with automated validation, PDF generation, and GitHub Pages deployment.

## Overview

This repository implements a **docs-as-code** approach for curriculum management, ensuring:

- **Single Source of Truth**: All curriculum content lives in one place
- **Version Control**: Full change history and governance via Git
- **Golden Rule Compliance**: Immutable 280-hour structure (240 core + 40 math)
- **Multi-Format Output**: Web documentation and PDF from the same source
- **Automated Validation**: CI/CD enforcement of hour totals
- **ANEW Brand Standards**: Professional styling following brand guidelines

## Golden Rule Hours Structure

The curriculum follows an immutable "Golden Rule" hour structure:

- **Core Hours**: 240 hours (excluding mathematics)
- **Math Hours**: 40 hours
- **Total**: 280 hours

All changes must maintain this structure. The build process validates hours automatically.

## Access the Curriculum

- **Web**: Browse the curriculum at [GitHub Pages](https://mandy1eigh007.github.io/curriculum_master/)
- **PDF**: Download the complete curriculum as [PDF](/downloads/curriculum.pdf)

## Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mandy1eigh007/curriculum_master.git
   cd curriculum_master
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright (required for PDF generation)**:
   ```bash
   playwright install chromium
   ```

4. **Serve locally with live reload**:
   ```bash
   mkdocs serve
   ```
   
   Visit `http://127.0.0.1:8000` in your browser.

5. **Build static site**:

```bash
mkdocs build
```

The built site will be in the `site/` directory. The PDF will be available at `site/downloads/curriculum.pdf`.

## Validate Golden Rule Hours

Before making changes, validate the Golden Rule hours:

```bash
python scripts/validate_golden_rule.py
```

This script checks that:
- Core hours (excluding math) = 240
- Math hours = 40
- Total hours = 280
- Each bucket's subunits sum correctly

## Adding Content

### Content Structure

All curriculum content follows this standard structure:

```markdown
# Module Name

## Required Hours
- **Total Hours**: X hours
- **Session Pattern**: Description

## Purpose
Brief description of why this module exists.

## Learning Outcomes
Students will be able to:
- Outcome 1
- Outcome 2
- Outcome 3

## Core Content
[Main content goes here]

## Deliverables
- Deliverable 1
- Deliverable 2
```

### Adding New Modules

1. Create a new Markdown file in the appropriate `docs/curriculum/` subdirectory
2. Follow the standard content structure above
3. Update `mkdocs.yml` navigation to include the new module
4. If adding hours, update `curriculum_data/golden_rule_hours.yaml` (maintaining Golden Rule)
5. Run validation: `python scripts/validate_golden_rule.py`

### Formatting Guidelines

- Use Markdown formatting consistently
- **No decorative icons or emojis** in content text
- Use headings hierarchically (h1 → h2 → h3)
- Use bullet points for lists
- Use code blocks for code examples

## Change Control & Governance

### Protected Branch

The `main` branch is protected and requires:
- Pull request reviews before merging
- Passing CI validation (Golden Rule hours, build)
- No direct commits allowed

### Pull Request Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-change-description
   ```

2. **Make your changes** following content guidelines

3. **Validate locally**:
   ```bash
   python scripts/validate_golden_rule.py
   mkdocs build
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-change-description
   ```

5. **Create a Pull Request** on GitHub

6. **CI will validate**:
   - Golden Rule hours are correct
   - Documentation builds successfully
   - PDF generates without errors

7. **After approval**, merge to main

### Release Tags (Optional)

Use Git tags to mark curriculum releases:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```
>>>>>>> origin/main

## Repository Structure

```
curriculum_master/
├── .github/
│   └── workflows/
│       └── pages.yml          # GitHub Actions for Pages deployment
├── curriculum_data/
│   └── golden_rule_hours.yaml # Golden Rule hour definitions
├── docs/
│   ├── curriculum/            # Curriculum content modules
│   ├── governance/            # Governance documentation
│   ├── stylesheets/
│   │   ├── extra.css         # Web styles (ANEW branding)
│   │   └── pdf.css           # PDF-specific styles
│   └── index.md              # Homepage
├── scripts/
│   └── validate_golden_rule.py # Validation script
├── .gitignore
├── CHANGELOG.md
├── mkdocs.yml                 # MkDocs configuration
├── README.md
└── requirements.txt           # Python dependencies
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

- **Single Source of Truth:** All curriculum content exists in one location only
- **No Master-Copy Drift:** Protected branch prevents direct commits
- **Pull Request Workflow:** All changes require review via PR
- **Golden Rule Validation:** CI automatically validates hour totals

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
=======
│       └── pages.yml          # GitHub Actions for Pages deployment
├── curriculum_data/
│   └── golden_rule_hours.yaml # Golden Rule hour definitions
├── docs/
│   ├── curriculum/            # Curriculum content modules
│   ├── governance/            # Governance documentation
│   ├── stylesheets/
│   │   ├── extra.css         # Web styles (ANEW branding)
│   │   └── pdf.css           # PDF-specific styles
│   └── index.md              # Homepage
├── scripts/
│   └── validate_golden_rule.py # Validation script
├── .gitignore
├── CHANGELOG.md
├── mkdocs.yml                 # MkDocs configuration
├── README.md
└── requirements.txt           # Python dependencies
```

## ANEW Brand Standards

This curriculum follows ANEW Brand Standard Guidelines:

- **Primary Typeface**: Helvetica Neue, Helvetica, Arial, sans-serif
- **Colors**:
  - Blue: `#326691`
  - Green: `#3FAE49`
  - Gray: `#505858`

Styles are defined in `docs/stylesheets/extra.css` and `docs/stylesheets/pdf.css`.

## Support

For questions or issues:

- Open an issue on GitHub
- Review governance documentation in `docs/governance/`
- Check existing issues on GitHub
- Contact repository administrators

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes.

## Acknowledgments

- Built with [MkDocs](https://www.mkdocs.org/)
- Theme: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- PDF Export: [mkdocs-exporter](https://github.com/adrienbrault/mkdocs-exporter)

## License

[Add appropriate license information]
