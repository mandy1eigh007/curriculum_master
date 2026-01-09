# Repository instructions for GitHub Copilot (curriculum_master)

This repository is an ANEW construction pre-apprenticeship curriculum docs-as-code system (MkDocs + optional PDF export).
Do not introduce or reintroduce “software curriculum” content (programming, web dev, backend, etc.). If you find remnants of those placeholders in nav/content, treat it as a defect and remove/disable them rather than expanding them.

Non-negotiables
- Do not invent facts, modules, hours, policies, or requirements. Use existing repo sources.
- Keep curriculum hours constraints aligned with Golden Rule enforcement in this repo.
- Keep PRs tight: only change what the issue asks for.

Build/validation commands (run before finishing)
- `pip install -r requirements.txt`
- `python scripts/validate_golden_rule.py`
- `mkdocs build --clean`

PDF behavior
- CI is intended to verify PDF generation on main branch builds, while PR builds can run without PDF.
Do not change this behavior unless explicitly requested.

Quality bar
- If you touch `mkdocs.yml`, ensure nav entries point to real files and builds do not emit “nav references not found” warnings.
- Do not commit large artifacts (zips, generated site output, generated PDFs) unless explicitly requested.

Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): 2026-01-09 15:04:01
Current User's Login: mandy1eigh007