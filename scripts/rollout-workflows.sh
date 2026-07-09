#!/usr/bin/env bash
# rollout-workflows.sh
#
# Copies the update-sbom.yml and weekly-docs.yml workflows from project-template
# to all circle6systems repos (that are cloned locally), creates a branch, and opens a PR.
#
# Prerequisites:
#   1. ANTHROPIC_API_KEY org secret must be set on circle6systems
#   2. gh CLI must be authenticated
#
# Usage:
#   ./scripts/rollout-workflows.sh [repo-name]   # single repo
#   ./scripts/rollout-workflows.sh --all          # all local repos

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE_DIR="$(dirname "$SCRIPT_DIR")"
GITHUB_DIR="$(dirname "$TEMPLATE_DIR")"
BRANCH="auto/add-doc-workflows"

WORKFLOWS=(
  ".github/workflows/update-sbom.yml"
  ".github/workflows/weekly-docs.yml"
)

rollout_repo() {
  local repo_path="$1"
  local repo_name
  repo_name="$(basename "$repo_path")"

  if [ "$repo_name" = "project-template" ]; then
    echo "SKIP: $repo_name (source template)"
    return
  fi

  if [ ! -d "$repo_path/.git" ]; then
    echo "SKIP: $repo_name (not a git repo)"
    return
  fi

  echo "--- Processing: $repo_name ---"
  cd "$repo_path"

  # Ensure .github/workflows exists
  mkdir -p .github/workflows

  # Check if workflows already exist and are identical
  local needs_update=false
  for wf in "${WORKFLOWS[@]}"; do
    if [ ! -f "$wf" ] || ! diff -q "$TEMPLATE_DIR/$wf" "$wf" > /dev/null 2>&1; then
      needs_update=true
      break
    fi
  done

  if [ "$needs_update" = false ]; then
    echo "SKIP: $repo_name (workflows already up to date)"
    return
  fi

  # Create branch from main
  git checkout main 2>/dev/null || git checkout master 2>/dev/null
  git pull --ff-only origin HEAD 2>/dev/null || true
  git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH" 2>/dev/null

  # Copy workflows
  for wf in "${WORKFLOWS[@]}"; do
    cp "$TEMPLATE_DIR/$wf" "$wf"
  done

  git add .github/workflows/update-sbom.yml .github/workflows/weekly-docs.yml
  if git diff --cached --quiet; then
    echo "SKIP: $repo_name (no changes after copy)"
    git checkout main 2>/dev/null || git checkout master 2>/dev/null
    return
  fi

  git commit -m "ci: add automated SBOM and weekly docs workflows"
  git push -u origin "$BRANCH"

  gh pr create \
    --title "ci: add automated SBOM and weekly docs workflows" \
    --body "$(cat <<'EOF'
## Summary

Adds two GitHub Actions workflows from the project template:

- **update-sbom.yml** -- Regenerates SBOM.md on every push to main using Claude Code
- **weekly-docs.yml** -- Weekly documentation refresh via Claude Code (opens a PR with changes)

## Prerequisites

The `ANTHROPIC_API_KEY` repository secret must be set. Run:
```bash
gh secret set ANTHROPIC_API_KEY --org circle6systems --visibility all
```

## Test plan

- [ ] Verify ANTHROPIC_API_KEY secret is configured
- [ ] Merge and push to main to trigger SBOM update
- [ ] Manually trigger weekly-docs via workflow_dispatch to verify

---
*Rolled out from project-template*
EOF
)" \
    --base main \
    --head "$BRANCH" || echo "PR may already exist for $repo_name"

  git checkout main 2>/dev/null || git checkout master 2>/dev/null
  echo "DONE: $repo_name"
}

# --- Main ---

if [ "${1:-}" = "--all" ]; then
  for dir in "$GITHUB_DIR"/*/; do
    if [ -d "$dir/.git" ]; then
      rollout_repo "$dir"
    fi
  done
elif [ -n "${1:-}" ]; then
  repo_path="$GITHUB_DIR/$1"
  if [ ! -d "$repo_path" ]; then
    echo "Error: $repo_path does not exist"
    exit 1
  fi
  rollout_repo "$repo_path"
else
  echo "Usage: $0 [repo-name | --all]"
  echo ""
  echo "Examples:"
  echo "  $0 wa-bill-tracker        # single repo"
  echo "  $0 --all                   # all local repos"
  exit 1
fi
