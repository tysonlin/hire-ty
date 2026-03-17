# Sub-Agent: ATS Analyzer

## Purpose

Simulate the behaviour of an Applicant Tracking System (ATS) to score the current CV draft for keyword presence and format compatibility before submission.

## Inputs

1. The current CV draft (`cv.typ` source or extracted plain text).
2. The structured job description (`job-description.md` from the relevant `/jobs/` folder).

## Tasks

### 1. Keyword extraction

- Extract all hard-skill keywords from the job description: technologies, tools, certifications, methodologies, and role-specific terminology.
- Extract soft-skill keywords explicitly mentioned (e.g. "cross-functional collaboration", "stakeholder management").
- Flag any keyword that appears in the JD **and** in `/data/tyson/` but is **missing** from the current CV draft.

### 2. Keyword density check

- Count occurrences of each required keyword in the CV.
- Identify keywords that appear zero times (critical gap) or only once (low coverage).
- Suggest natural placements for missing keywords without making the text feel stuffed.

### 3. Format compatibility check

Verify the CV structure against common ATS parsing requirements:

| Check | Pass criteria |
|-------|---------------|
| Contact information is in the top section | Name, email, phone, LinkedIn present in header |
| Section headings are standard | e.g. Experience, Education, Skills — no creative headings like "My Journey" |
| Dates are machine-readable | Use `Month YYYY – Month YYYY` or `YYYY – YYYY` |
| No tables used for core content | Tables confuse many ATS parsers; use them only for Skills if unavoidable |
| No text boxes or columns for body content | Single-column layout for experience and education |
| No images or icons | ATS systems ignore or reject embedded images |
| File will export to clean PDF | Typst produces ATS-friendly PDFs when using the standard template |

### 4. Score and report

Produce a short report with:

- **Keyword coverage score:** `X / Y keywords matched` with a percentage.
- **Format issues:** list any failed format checks with a one-line fix suggestion.
- **Recommended additions:** up to 5 specific keyword insertion suggestions with the exact sentence or bullet point to modify.

## Output

Return a structured Markdown report. Example:

```markdown
## ATS Analysis Report

**Keyword coverage:** 18 / 24 (75%)

### Missing keywords
- `Kubernetes` — present in JD and profile, missing from CV Experience section
- `stakeholder management` — present in JD, not in current draft

### Format issues
- None

### Recommended additions
1. In the "[Company] – [Role]" bullet, add "…deployed on Kubernetes" to the infrastructure sentence.
2. Add "stakeholder management" to the Skills section under Leadership.
```

## Constraints

- Follow all rules in `/constraints/content-guidelines.md`.
- Do **not** invent new facts. Only surface keywords that are substantiated in `/data/tyson/`.
- Pass your report to the **Conflict Resolver** sub-agent if any recommendation contradicts another sub-agent's output.
