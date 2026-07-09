---
title: Accessibility
scope: Accessibility commitments for this repo's docs and tooling
last_updated: 2026-07-09
---

# Accessibility

This repo is documentation plus a small Python CLI validator. Accessibility is
treated as a first-class quality attribute.

## Documentation

- Plain language; abbreviations defined on first use (VNA, IL, PL/CTCSS, etc.).
- Real Markdown tables for tabular data, with header rows - not ASCII art.
- Descriptive link text and relative paths, not "click here".
- No information conveyed by color alone; status is always spelled out in words.
- Logical heading hierarchy, no skipped levels.
- Short lines in code blocks; each block says what it does.

## CLI (`tools/validate_inventory.py`)

- `--help` with usage examples.
- `--json` machine-readable output option.
- Text-labeled status (`[OK]`, `[ERROR]`) alongside any formatting - never color
  alone.
- Non-zero exit code on failure; error messages state the file and the problem.

## Reporting

Open an issue using the accessibility template in
`.github/ISSUE_TEMPLATE/`. Accessibility issues are severity-critical by default.
