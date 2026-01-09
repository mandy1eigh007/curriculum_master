# ANEW Curriculum Master

Welcome to the ANEW Curriculum Master repository - the single source of truth for all curriculum content.

## Overview

This repository implements a **docs-as-code** approach for curriculum management, ensuring:

- **Single Source of Truth**: All curriculum content lives in one place
- **Version Control**: Full change history and governance via Git
- **Golden Rule Compliance**: Immutable 280-hour structure (240 core + 40 math)
- **Multi-Format Output**: Web documentation and PDF from the same source

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

3. **Run the development server**:
   ```bash
   mkdocs serve
   ```
   
   Visit `http://127.0.0.1:8000` in your browser.

### Generate PDF

To generate the PDF locally:

```bash
mkdocs build
```

The PDF will be available at `site/downloads/curriculum.pdf`.

### Validate Golden Rule Hours

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

## License

[Add appropriate license information]
