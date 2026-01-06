# ANEW Curriculum

Welcome to the ANEW Curriculum documentation. This is a docs-as-code implementation optimized for the immutable "Golden Rule" hour structure.

## Golden Rule Hour Structure

The curriculum follows a strict hour allocation:

- **Core Curriculum (excluding Mathematics):** 240 hours
- **Mathematics:** 40 hours
- **Total:** 280 hours

## Curriculum Structure

The curriculum is organized into the following major areas:

### Foundations (60 hours)
Introduction to foundational concepts and skills required for the program.

### Development (80 hours)
Core development skills and practices.

### Advanced Topics (60 hours)
Advanced concepts building on foundational knowledge.

### Capstone (40 hours)
Culminating project demonstrating mastery of curriculum objectives.

### Mathematics (40 hours)
Applied mathematics essential for program success.

## Download PDF

PDF versions of individual pages can be generated using the mkdocs-exporter plugin.

To enable PDF generation locally, uncomment the exporter plugin in `mkdocs.yml` and rebuild:

```bash
# In mkdocs.yml, uncomment:
# - exporter

mkdocs build
```

Individual PDF files will be available for each page in the built site.

## Quick Start

### Local Development

To build and preview this documentation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright for PDF generation
playwright install chromium

# Serve locally (live reload)
mkdocs serve

# Build static site
mkdocs build
```

### Generating PDF

The PDF is automatically generated during the build process. To generate it manually:

```bash
mkdocs build
```

The PDF will be output to `site/downloads/curriculum.pdf`.

## Governance

This repository implements strict governance controls:

- **Single Source of Truth:** All curriculum content exists in one location only
- **No Master-Copy Drift:** Protected branch prevents direct commits
- **Pull Request Workflow:** All changes require review via PR
- **Golden Rule Validation:** CI automatically validates hour totals

See the [Governance](governance/overview.md) section for complete details.

## Adding Content

All curriculum content is written in Markdown with consistent formatting:

1. No icons or emojis in content
2. Standard section structure (see templates in curriculum folders)
3. Follow ANEW Brand Standards for styling

## Change Control

See [Change Control](governance/change-control.md) for information on:

- Creating pull requests
- Review process
- Release tagging (optional)
- Golden Rule validation

## Brand Standards

This documentation follows ANEW Brand Standard Guidelines:

- **Primary Typeface:** Helvetica Neue, Helvetica, Arial, sans-serif
- **Colors:**
  - Blue: #326691
  - Green: #3FAE49
  - Gray: #505858

All styling is defined in `docs/stylesheets/extra.css` and `docs/stylesheets/pdf.css`.
