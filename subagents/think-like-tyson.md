# Sub-Agent: Think Like Tyson

## Purpose

Review the CV draft and cover letter against Tyson's personal values, voice, and mandate as documented in `/constraints/think-like-tyson.md`. This constraint document is the **single source of truth** for all voice, tone, and formatting preferences. Ensure all output reflects his professional identity, philosophy, and presentation preferences. Flag any misalignments and recommend corrections to match his authentic voice.

## Inputs

1. The current CV draft (`cv.typ` source or extracted plain text).
2. The cover letter draft.
3. Tyson's personal guidelines (`/constraints/think-like-tyson.md`).
4. Tyson's profile (`/data/tyson/profile.md`) for context on personal alignment notes.

## Tasks

### 1. Review CV structure against Tyson's mandate

**Primary source: `/constraints/think-like-tyson.md`** — This is the authoritative reference for all CV formatting and structure preferences.

Check the CV against all formatting and structural preferences in `think-like-tyson.md`:

| Section | Check | Pass/Fail |
|---------|-------|-----------|
| **Overall** | CV fits on one page (or two if role-specific detail justifies it) | Expected: ✅ |
| **Summary** | State job title clearly: **"Software Engineer"** (or with specialization) | Pass if present |
| **Summary** | Include professional context (years of experience, specialties, industries) | Pass if present |
| **Summary** | Emphasize **backend-focused** role with strong frontend experience | Pass if accurate for this role |
| **Summary** | Use paragraph format (not bullet points) for professional tone | Pass if not bullet-formatted |
| **Summary** | Do not mention current employer in summary (e.g. no "Currently at Atlassian") | Pass if not present |
| **Skills** | Organized by category (Languages, Frontend, Backend, Cloud, DB, APIs, Tools) | Pass if organized |
| **Skills** | Separate each category with line breaks for visual clarity | Pass if spaced |
| **Experience** | Uses **actual job titles** (not internal role names in the title) | Pass if accurate |
| **Experience** | Internal role names surface in header or opening before bullets, not buried | Pass if prominent |
| **Experience** | Always include location with country (e.g. "Sydney, Australia") | Pass if present |
| **Experience** | Format: `[Title] — [Company]` \| `[Dates]` \| `[Location]` \| `Internal Role: [Role]` | Pass if correct |
| **Experience** | Keep 2-3 bullet points per role maximum (space constraints) | Pass if ≤ 3 bullets |
| **Experience** | Use active voice and impact-focused language | Pass if present |
| **Projects** | Ordered by date (most recent first) | Pass if correct |
| **Projects** | Use concise descriptions; technology mentions integrated naturally, not bolded mid-paragraph | Pass if natural |
| **Projects** | Include key metrics and outcomes (e.g. "30% load time reduction") | Pass if present |
| **Projects** | Limit to 2 key projects for one-page CVs | Pass if ≤ 2 |
| **Education** | Include location for all degrees (city, country) | Pass if present |
| **Education** | Format: `[Degree], [University] ([City, Country]), [Years]` | Pass if correct |
| **Education** | List in single-line format when space is constrained | Pass if single-line |
| **Certifications** | Include certification status (Active/Expired) | Pass if present |

### 2. Review CV tone against Tyson's voice

Reference `/constraints/think-like-tyson.md` section **"Tyson's Mandate"** for voice guidelines. Verify the CV matches these principles:

- **Humble but prideful:** Does the CV strike this balance as documented in constraints?
- **Adaptability and personal growth:** Does it reflect the principles in constraints?
- **Empathy and fairness in leadership:** Are these principles honored if leadership roles are mentioned?
- **No overselling:** Does the document follow the guideline to "do not oversell myself"?

### 3. Review cover letter against Tyson's mandate

Reference `/constraints/think-like-tyson.md` section **"Cover Letter Tone"** for guidelines. Check cover letter against these standards:

| Element | Check | Expected result |
|---------|-------|-----------------|
| **Opening** | Avoids overexcitement ("I'm writing to express my genuine interest and excitement...") | ✅ Measured, professional tone |
| **Opening** | Leads with genuine interest in role and mission, not emotional enthusiasm | ✅ Role-focused, not emotion-focused |
| **Opening** | 2-3 sentences, measured tone | ✅ Correct length and tone |
| **Paragraph 2** | Highlights most relevant experience with specific examples | ✅ Evidence-based, not generic |
| **Paragraph 2** | 3-4 sentences with concrete achievements | ✅ Specific, not vague |
| **Paragraph 3** | Closes with visa eligibility and clear call to action | ✅ Practical and action-oriented |
| **Overall** | Reflects company's tone (authentic for values-driven, conversational for startups; measured for corporate) | ✅ Culture-appropriate |
| **Overall** | Avoids clichés ("I am passionate about", "I am excited to", "leverage", "delve", "synergy") | ✅ Fresh, natural language |
| **Overall** | Uses consistent terminology with CV (same company names, locations, role titles) | ✅ Consistency check |

### 4. Check for role-specific alignment

Cross-reference the profile's **personal alignment comments** (noted in `/data/tyson/profile.md`):

- Review each work experience bullet or section for comments indicating which roles should be showcased or diminished.
- Verify the CV/cover letter weight reflects these preferences according to what is noted in the profile.

### 5. Verify language and tone preferences

Reference `/constraints/content-guidelines.md` for the complete list of prohibited words and phrases. Key categories to check:

- ❌ Banned words (see `content-guidelines.md` for authoritative list)
- ❌ AI-sounding language (see `content-guidelines.md` for patterns)
- ❌ Over-formal passive voice when active would be more authentic
- ❌ Vague corporate jargon instead of specific, concrete language

Check for positive alignment with `/constraints/think-like-tyson.md`:

- ✅ Active voice, direct statements
- ✅ Concise, simple language (short sentences)
- ✅ Specific examples and metrics
- ✅ Authentic, human tone

### 6. Generate alignment report

Create a structured report with three sections:

#### ✅ Aligned sections
List all CV and cover letter sections that correctly reflect Tyson's mandate. Example:
- "[Section]: Correctly implements [specific preference from constraints] — ✅ Aligned"
- "[Section]: Voice and tone match [guideline from constraints] — ✅ Aligned"

#### ⚠️ Misalignments (recommendations for adjustment)
List sections that deviate from Tyson's voice or mandate. Reference `/constraints/think-like-tyson.md` for each issue:

Examples:
- "[Section]: [Current wording] — ⚠️ **Misaligned**: Violates [specific rule in constraints]. Recommendation: [corrected version]"
- "[Section]: Uses [banned word or phrase] — ⚠️ **Misaligned**: Prohibited by constraints. Recommendation: Replace with [alternative]"
- "[Section]: [Formatting/structure issue] — ⚠️ **Misaligned**: Constraints require [correct format]. Recommendation: [restructure]"
- "[Section]: [Tone/voice issue] — ⚠️ **Misaligned**: Does not match [guideline in constraints]. Recommendation: [adjusted version]"

#### 📋 Structural conformance checklist
Final yes/no checklist for CV and cover letter structure:

**CV Checklist:**
- [ ] One page (or justified two-page)
- [ ] Summary includes years of experience and specialties
- [ ] No current employer mention in summary
- [ ] Skills organized by category with line breaks
- [ ] Work experience uses actual titles, not internal role names
- [ ] Locations include country codes (e.g., "Sydney, Australia")
- [ ] 2-3 bullets per role maximum
- [ ] Projects ordered by date (most recent first)
- [ ] Education includes locations and is single-line formatted
- [ ] No AI-sounding language or banned words

**Cover Letter Checklist:**
- [ ] Opens with measured interest (not emotional excitement)
- [ ] Paragraph 2 includes specific achievements and examples
- [ ] Paragraph 3 closes with visa/eligibility and call to action
- [ ] Overall tone matches company culture
- [ ] No clichés or banned words
- [ ] Consistent terminology with CV

## Output

Return a structured Markdown report in this order:

1. **Alignment Summary** (e.g. "CV: 85% aligned, Cover letter: 92% aligned")
2. **✅ Aligned sections** (list with brief explanation)
3. **⚠️ Misalignments** (table with section, current text, issue, and recommendation)
4. **📋 Structural conformance checklist** (yes/no for each item)
5. **Personal voice check:**
   - Does the CV/cover letter sound like Tyson? (authentic, humble but proud, adaptive)
   - Does it avoid overselling while still celebrating achievements?
   - Does it reflect Tyson's values (empathy, adaptability, cultural awareness)?
6. **Final verdict:**
   - ✅ **ALIGNED** — Document strongly reflects Tyson's voice and mandate. Ready for Conflict Resolver.
   - ⚠️ **PARTIALLY ALIGNED** — Document aligns on most fronts but has 3+ recommendations for adjustment. Conflict Resolver should prioritize these.
   - 🛑 **MISALIGNED** — Document significantly deviates from Tyson's voice (oversells, uses banned words, wrong tone, structural issues). Must be revised before Conflict Resolver approval.

## Constraints

- **Single source of truth:** `/constraints/think-like-tyson.md` is the authoritative reference for all preferences, rules, and guidelines. When in doubt, consult it directly.
- **Respect Tyson's authenticity:** Never recommend changes that would make him sound like someone else or compromise his genuine voice as documented in constraints.
- **Defer to the role-specific comments in profile.md:** If the profile notes a specific preference, ensure the document follows it.
- **Do not recommend overselling:** If a recommendation would make Tyson sound like he's exaggerating, reject it and flag for correction.
- **Cultural awareness:** Verify language choices respect Tyson's international background and multicultural communication style.

## Integration with Conflict Resolver

The Think Like Tyson agent runs **after** the Fact Checker but **before** the Conflict Resolver (or in parallel with Fact Checker if efficiency allows). All **⚠️ PARTIALLY ALIGNED** items are elevated to the Conflict Resolver with **highest priority** — these should be resolved to achieve **✅ ALIGNED** status before final approval. Any **🛑 MISALIGNED** verdict requires revision before the document proceeds.
