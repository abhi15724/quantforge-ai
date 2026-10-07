#!/usr/bin/env bash
# Builds quantforge-ai.skill (a zip of the skill folder) for upload to Claude chat (web/desktop/mobile).
set -euo pipefail
cd "$(dirname "$0")/skills"
rm -f ../quantforge-ai.skill
zip -rq ../quantforge-ai.skill quantforge-ai -x '*/__pycache__/*'
echo "Built quantforge-ai.skill"
