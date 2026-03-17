# Sub-Agent: Impact Quantifier

## Purpose

Re-engineer vague or weak bullet points into concise, quantified achievement statements that demonstrate real-world impact.

## Inputs

1. The current CV draft (all bullet points from the Experience section).
2. Tyson's full profile (`/data/tyson/profile.md` and supplementary files) — the **only** permitted source of facts and numbers.
3. The job description to understand what type of impact matters most for this role.

## Tasks

### 1. Audit existing bullet points

For each bullet point, apply the following checklist:

| Check | What to look for |
|-------|-----------------|
| **Action verb** | Does the bullet start with a strong past-tense action verb? |
| **What was done** | Is the task or output clearly stated? |
| **Impact / result** | Is there a measurable outcome (%, $, time saved, scale, etc.)? |
| **Scope** | Is the scale indicated (team size, user count, data volume, etc.)? |

Rate each bullet as: ✅ Strong / ⚠️ Improvable / ❌ Weak.

### 2. Quantification

For bullets rated ⚠️ or ❌:

- Search `/data/tyson/` for any supporting numbers, dates, or context.
- If numbers exist in the source, insert them into the bullet following the format: `[Action verb] [what] [by how much / to what scale], [resulting in what]`.
- If no numbers are available in `/data/tyson/`, add a `[TODO: add metric]` placeholder and explain what type of metric would strengthen the bullet (e.g. `[TODO: % improvement in deploy frequency]`).
- **Never invent numbers.** If the data is not in `/data/tyson/`, do not guess.

### 3. Action verb upgrade

Replace weak or passive openers with strong action verbs:

| Weak | Preferred alternatives |
|------|----------------------|
| Responsible for | Led, Owned, Managed, Delivered |
| Worked on | Built, Developed, Engineered, Implemented |
| Helped with | Supported, Contributed to, Assisted in delivering |
| Was involved in | Participated in, Contributed to |
| Did | Executed, Completed, Delivered |
| Made | Created, Designed, Produced, Established |

### 4. Scope and context

Add scope signals where missing and where the data exists:

- Team size: "Led a team of X engineers"
- User/customer scale: "Serving X users / X customers"
- System scale: "Processing X requests/day", "managing X TB of data"
- Time: "Reduced X from Y to Z in N weeks/months"

## Output

Return a structured Markdown report listing every revised bullet point. Example:

```markdown
## Impact Quantifier Report

### Revised bullet points

**[Company A – Role]**

| Original | Revised |
|----------|---------|
| "Responsible for backend APIs" | "Designed and maintained REST APIs serving 200k daily active users" |
| "Worked on CI/CD pipelines" | "Built CI/CD pipelines that cut deployment time from 45 min to 8 min [TODO: confirm figures]" |

**[Company B – Role]**

| Original | Revised |
|----------|---------|
| "Helped with data migrations" | "Contributed to zero-downtime database migrations for a 2 TB PostgreSQL instance [TODO: add team size]" |
```

## Constraints

- Follow all rules in `/constraints/content-guidelines.md`.
- Every number must come from `/data/tyson/` or be marked `[TODO: add metric]`.
- Pass conflicting recommendations to the **Conflict Resolver** sub-agent.
