# /data/tyson — Tyson's Professional Information

This folder is the **single source of truth** for all CV and cover letter generation.

## Files to maintain

| File / Folder | Purpose |
|---------------|---------|
| `profile.md` | Core profile: personal details, work history, education, skills, projects |
| `certifications/` | (optional) PDF or image copies of certificates |
| `references.md` | (optional) Professional references (keep private; do not commit real contact details publicly) |
| `*.pdf` | (optional) Past CV/resume PDFs kept for reference |

## Rules

1. **Every fact here must be true.** The content-guard-rail in `/constraints/` enforces that generated documents only reference facts in this folder.
2. Keep information **up to date** — update this folder whenever your situation changes.
3. Use plain Markdown. Avoid HTML or complex formatting so the agent can parse it reliably.
