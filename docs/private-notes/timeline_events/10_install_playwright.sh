#!/bin/bash
# Timeline Event 10: Install Playwright and System Dependencies
# Date: January 8, 2026
# Description: Install Playwright browser and required system libraries

echo "=== Installing Playwright Browser ==="
python -m playwright install chromium

echo ""
echo "=== Installing System Dependencies ==="
# Installed various X11 and GTK libraries required for Chromium
sudo apt install -y libatk1.0-0t64 libatk-bridge2.0-0t64 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libxss1 libasound2t64 libxfixes3 libxext6 libxrender1 libxss1 libgtk-3-0