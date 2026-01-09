#!/bin/bash
# Timeline Event 2: Playwright Investigation
# Date: January 8, 2026
# Description: Search for Playwright references in requirements and workflows

echo "=== Playwright Search in Requirements ==="
grep -i "playwright" -n requirements.txt || echo "No Playwright in requirements.txt"

echo ""
echo "=== Playwright Search in Workflows ==="
grep -i "playwright" -R .github/workflows || echo "No Playwright in workflows"