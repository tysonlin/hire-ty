# Sub-Agent: Keyword Gap Agent

## Purpose

Identify semantic mismatches between the CV/cover letter draft and the job description — going beyond exact keyword matching to catch conceptual gaps and terminology differences.

## Inputs

1. The current CV and cover letter drafts.
2. The structured job description (`job-description.md`).
3. Tyson's full profile (`/data/tyson/profile.md` and any supplementary files).

## Tasks

### 1. Semantic gap analysis

- Map every significant concept in the job description to its closest equivalent in the CV.
- Flag cases where Tyson has the underlying experience but the CV uses different terminology than the JD.
- Identify genuinely missing competencies (skills or experience not evidenced in `/data/tyson/`) — **do not suggest fabricating these**.

### 2. Terminology alignment

For each semantic mismatch found, propose a terminology substitution that:

- Uses the JD's preferred phrasing.
- Remains factually accurate according to `/data/tyson/`.
- Does not violate any rule in `/constraints/content-guidelines.md`.

**Example:**

| CV phrasing | JD phrasing | Suggested change |
|-------------|-------------|-----------------|
| "built CI pipelines" | "continuous delivery automation" | Change to "automated continuous delivery pipelines" |
| "worked with stakeholders" | "stakeholder engagement" | Change to "managed stakeholder engagement" |

### 3. Missing narrative threads

Identify themes the JD emphasises that the CV does not address, such as:

- Leadership and team growth (if the role is senior).
- Customer or business impact (if the role is product/commercial-facing).
- Scale or complexity signals (if the JD mentions large systems, high traffic, or big teams).

For each missing narrative thread, suggest where in the CV it could be addressed using existing facts from `/data/tyson/`.

### 4. Over-indexing check

Flag areas where the CV spends disproportionate space on topics the JD does not prioritise. Suggest trimming or repositioning these sections.

## Output

Return a structured Markdown report. Example:

```markdown
## Keyword Gap Report

### Semantic mismatches (terminology to align)
| CV term | JD term | Recommended substitution |
|---------|---------|--------------------------|
| "built CI pipelines" | "continuous delivery automation" | "automated continuous delivery pipelines" |

### Missing narrative threads
- **Business impact:** JD emphasises commercial outcomes; CV lacks revenue/cost figures. Consider adding metrics from [role X] if available in profile.
- **Team leadership:** JD mentions "leading engineers"; CV mentions management but not growth or mentorship.

### Over-indexed sections
- "Open Source Contributions" section is long but not mentioned in JD. Consider condensing to two lines.
```

## Constraints

- Follow all rules in `/constraints/content-guidelines.md`.
- Do **not** suggest adding facts not found in `/data/tyson/`.
- Pass conflicting recommendations to the **Conflict Resolver** sub-agent.
