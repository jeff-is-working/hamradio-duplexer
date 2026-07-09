# Status Summary -- 2026-03-22 -- Org Migration

Date: 2026-03-22

## What was done

### 1. Automated documentation workflows

Created and deployed two GitHub Actions workflows:

- **update-sbom.yml** -- Regenerates SBOM.md on every push to main via Claude Code CLI (Sonnet)
- **weekly-docs.yml** -- Weekly enterprise documentation refresh, opens a PR for review (runs Sundays at ~3:17AM UTC)

Both workflows were committed to `circle6systems/project-template` and rolled out to all 16 circle6systems repos via PRs. All PRs were merged and corresponding issues closed.

### 2. ANTHROPIC_API_KEY org secrets

Configured org-level secrets for Claude Code CLI access:

- **circle6systems** -- visibility: selected (14 specific repos)
- **surveillancewatch** -- visibility: all
- **wa-bill-tracker** -- visibility: all
- **ilistwise** -- visibility: all
- **KGCP-Project** -- visibility: all

New orgs use `visibility:all` because Jeff is sole admin and all repos need the key.

### 3. Created 4 new GitHub orgs

- **surveillancewatch** (the name `wasurveillancewatch` was taken)
- **wa-bill-tracker**
- **ilistwise**
- **KGCP-Project**

### 4. Transferred 27 repos

**14 to surveillancewatch:**
surveillance-watch, flock_Hunter, oui-spy-too, ICEWatchRF, WavFox, trash-dump-to-rf-dump, hotspot_swarm, p25-streaming-platform, ESP-GlassHole, FCCDB_KF7ATW, ULS_Lookup_2025_GOVSHUTDOWN, CYD-Projects, wasurveillancewatch-dev, orbic-research

**6 to wa-bill-tracker:**
wa-bill-tracker, wa-bill-tracker-pro, Open_Government_Meeting_Knowledge, wa-bill-tracker-dev, wa-bill-tracker-enterprise, waleg-soap2rest

**3 to ilistwise:**
ilistwise, ilistwise-landing, ilistwise-admin

**4 to KGCP-Project:**
knowledge-graph-context-pipeline, offline-knowledge-stack, ai-knowledge-graph, image2knowledge_pipeline

**1 to circle6systems:**
CTI_Pipeline (transferred from jeff-is-working)

### 5. Updated Cloudflare DNS

- `wasurveillancewatch.org` CNAME -> `surveillancewatch.github.io` (was `jeff-is-working.github.io`)
- `wa-bill-tracker.org` CNAME -> `wa-bill-tracker.github.io` (was `jeff-is-working.github.io`)

Both verified responding HTTP 200.

### 6. Updated all local git remotes

All transferred repos had their local git remotes updated to point to the new org URLs.

### 7. Updated workspace CLAUDE.md

Added a multi-org routing table to the workspace-level CLAUDE.md so Claude knows which org each project belongs to.

### 8. Created GitHub Projects in each new org

**surveillancewatch:**
- Surveillance Watch Roadmap
- Hotspot Swarm
- FCCDB KF7ATW
- Org Setup and Migration Tracking

**wa-bill-tracker:**
- WA Bill Tracker UX Epic
- Thurston County Pipeline
- Open Govt Meeting Knowledge
- Org Setup and Migration Tracking

**ilistwise:**
- iListWise Product Roadmap
- Org Setup and Migration Tracking

**KGCP-Project:**
- KGCP CTI Platform Adapters
- Org Setup and Migration Tracking

### 9. Closed superseded projects

6 projects closed in jeff-is-working, 2 projects closed in circle6systems.

### 10. Created migration tracking issues

Migration summary issues and remaining-work issues were created in all orgs.

---

## Remaining work (tracked as GitHub issues)

- Create org project-template in each new org (surveillancewatch #11, wa-bill-tracker #61, ilistwise #100, KGCP-Project #18)
- Set up org teams for collaborators (surveillancewatch #14, wa-bill-tracker #64, ilistwise #102, KGCP-Project #20)
- Update external links for FCCDB_KF7ATW old Pages URL (surveillancewatch #12)
- Disable SBOM/weekly-docs workflows on inactive/archived repos (surveillancewatch #15)
- Create CONTRIBUTING.md and governance docs for KGCP-Project open-source repos (#21)
- circle6systems post-migration cleanup (#226)

---

## Lessons learned

- GitHub OAuth device flow (`gh auth login -w`) does not support the `project` scope -- must use a Personal Access Token (classic) for `gh project` commands.
- The gh CLI does not have a `repo transfer` command -- must use the GitHub API directly (`POST /repos/{owner}/{repo}/transfer`).
- Repo transfers are async but typically complete within seconds.
- GitHub Pages config (custom domain, HTTPS enforcement) is preserved during transfer, but DNS must be updated manually.
- When re-authenticating gh CLI, the new token replaces the old one -- all scopes from the previous token are lost unless re-requested.
- Org-level secrets with `visibility:all` are appropriate for single-admin orgs where all repos need the secret.
