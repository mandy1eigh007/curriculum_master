#!/bin/bash
# Timeline Event 1: Initial Git Status Check
# Date: January 8, 2026
# Description: Check initial repository status and branch information

echo "=== Initial Repository Check ==="
git status
echo ""
git branch --show-current
echo ""
git log -1 --oneline