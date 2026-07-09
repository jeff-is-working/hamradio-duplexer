---
title: Project Standards
scope: Development workflow, branching, issue standards, code quality, and documentation
last_updated: 2026-03-27
---

# CLAUDE.md — Project Standards

These instructions govern all development work in this repository. They are mandatory and override default behavior.

---

## Development Workflow

**All work must follow this sequence — no exceptions.**

1. **Issues first.** Every code change must map to a documented GitHub issue. The issue must include a remediation/implementation plan before any code is written. Do not write code for work that isn't tracked in an issue.
2. **Tests before code.** Write tests for the expected behavior before writing implementation code (TDD). If the repo has no test infrastructure, set it up as the first task before any feature work.
3. **Plan, then implement.** Use plan mode to design the approach, get alignment, then execute. Do not start coding without a plan for non-trivial work.
4. **Never suppress failing tests.** If a test fails, file a GitHub issue for the root cause and leave the test failing until the underlying problem is fixed. Do not add filters, skip conditions, or workarounds to make failing tests pass. Fix the problem, not the test.

---

## Branching & Commits

- Create feature branches from `main` (e.g., `sprint-1/critical-fixes`, `feature/user-auth`)
- One commit per issue for clean history
- Write concise commit messages that explain the "why", not just the "what"
- PR back to `main` when work is complete; do not merge without review

---

## Issue Standards

Every GitHub issue must include:

- **Problem/Objective**: What needs to change and why
- **Location**: Files, functions, or components affected
- **Implementation Plan**: Step-by-step remediation or implementation approach
- **Testing**: Specific test cases to write before implementation
- **Verification**: How to confirm the fix/feature works end-to-end

---

## Code Quality

- Do not write code without reading the existing codebase first
- Follow existing patterns and conventions in the repo
- Validate inputs at system boundaries (user input, external APIs)
- Do not add features, refactoring, or "improvements" beyond what the issue specifies
- Keep solutions simple — the right amount of complexity is the minimum needed

---

## Documentation

- `docs/status/` -- Status reports and session summaries (date-prefixed, e.g., `2026-03-21-sprint-review.md`)
- Do not create documentation files unless explicitly requested
- Keep CLAUDE.md up to date as the project evolves

## End-of-Session Documentation

Before closing any work session, complete these steps:

1. **Status file.** Write a date-prefixed summary to `docs/status/` covering: what was done, decisions made, what's left, and lessons learned.
2. **Commit and push.** All changes (including status docs) must be committed and pushed. No dangling local-only work.
3. **Verify clean state.** Run `git status` to confirm no uncommitted changes.

---

## What NOT to Do

- Do not write code for work that isn't tracked in a GitHub issue
- Do not write implementation code before tests
- Do not skip the plan-first workflow for non-trivial changes
- Do not push to `main` directly — use feature branches and PRs
- Do not add Circle6Systems / C6S branding unless explicitly requested
