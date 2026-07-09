#!/usr/bin/env bash
# setup-secrets.sh
#
# Sets the ANTHROPIC_API_KEY secret on jeff-is-working repos.
# Since jeff-is-working is a user account (not an org), secrets must be set per-repo.
#
# Usage:
#   ./scripts/setup-secrets.sh                    # prompted for key, sets on all repos
#   ./scripts/setup-secrets.sh wa-bill-tracker    # single repo
#
# The script will prompt for the API key once and apply it to all target repos.

set -euo pipefail

SECRET_NAME="ANTHROPIC_API_KEY"
OWNER="circle6systems"

# Get the API key
if [ -t 0 ]; then
  echo -n "Enter your Anthropic API key: "
  read -rs API_KEY
  echo ""
else
  read -r API_KEY
fi

if [ -z "$API_KEY" ]; then
  echo "Error: API key cannot be empty"
  exit 1
fi

set_secret() {
  local repo="$1"
  echo -n "Setting $SECRET_NAME on $OWNER/$repo... "
  echo "$API_KEY" | gh secret set "$SECRET_NAME" --repo "$OWNER/$repo" 2>&1 && echo "OK" || echo "FAILED"
}

if [ -n "${1:-}" ]; then
  set_secret "$1"
else
  # Get all repos
  repos=$(gh repo list "$OWNER" --limit 100 --json name --jq '.[].name')
  for repo in $repos; do
    set_secret "$repo"
  done
fi
