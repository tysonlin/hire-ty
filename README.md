# HireTy

An agentic workflow repository to help Tyson Lin get hired — faster and better.

The agent takes Tyson's professional profile, a job description, and produces a tailored CV (compiled to PDF via Typst) and a cover letter, all optimised through a pipeline of specialised sub-agents.

---

## Repository structure

```
hire-ty/
├── data/
│   └── tyson/            # Tyson's professional profile, skills, and work history
│       ├── README.md     # How to maintain this folder
│       └── profile.md    # Master profile (fill this in first)
├── jobs/                 # One sub-folder per job application
│   └── README.md         # Folder naming convention and workflow
├── constraints/
│   └── content-guidelines.md  # Content rules all output must follow
├── subagents/            # Instructions for each specialised agent
│   ├── fact-checker.md
│   ├── think-like-tyson.md
│   ├── ats-analyzer.md
│   ├── keyword-gap-agent.md
│   ├── impact-quantifier.md
│   ├── tone-optimizer.md
│   ├── conflict-resolver.md
│   └── change-composer.md
├── Typst.md              # How to install Typst and compile CVs
└── README.md             # This file
```

---

## Prerequisites

### 1. Fill in your profile

Open `data/tyson/profile.md` and complete every section with accurate, factual information. This is the only source of truth the agent uses — everything generated will be based on what you put here.

### 2. Install Typst (for compiling CVs to PDF)

See **`Typst.md`** for full installation instructions for macOS, Windows, and Linux.

Quick install:

```bash
# macOS
brew install typst

# Windows — download from https://github.com/typst/typst/releases

# Linux (Debian/Ubuntu)
sudo apt install typst
```

Verify:

```bash
typst --version
```

### 3. AI model / agent runner

This repository is designed to be used with an AI coding agent (e.g. GitHub Copilot Workspace, Claude, GPT-4, or any agent that can read files and follow instructions). No specific platform is required — the agent instructions are plain Markdown files that any capable model can follow.

### 4. (Optional) Set up PII Detection Pre-Commit Hook

To protect your personal information from being accidentally committed to Git, you can optionally set up an AI-powered pre-commit hook that scans for PII before each commit.

**This is completely optional** — your code will work fine without it. But if you're sharing this repo or want an extra safety layer, follow these steps:

```bash
# 1. Ensure Python 3 is installed
# macOS: brew install python3
# Linux: sudo apt install python3
# Windows: https://www.python.org/downloads/

# 2. Copy the example configuration
cp .env.example .env

# 3. Edit .env and add your API key (Anthropic or OpenAI)
nano .env

# 4. Install the required Python package
pip install anthropic  # or: pip install openai
```

That's it! The hook is already installed. On your next commit, it will scan for PII and block the commit if any is detected.

For full details, see **`.githooks/README.md`**.

---

## How to apply for a job

### Step 1 — Provide the job description

Give the agent a job description. Either:
- Paste the full text of the JD, or
- Provide the URL and ask the agent to fetch and summarise it.

### Step 2 — The agent creates the job folder

The agent will create a folder under `/jobs/` named:

```
<Company Name> - <Job Title> - <City>, <Country>
```

And populate it with:

| File | Contents |
|------|----------|
| `job-description.md` | Structured summary of the JD |
| `cv.typ` | Typst source for your tailored CV - this should be generated per job position |
| `cover-letter.md` | Tailored cover letter in email format |

### Step 3 — Run the sub-agent pipeline

The agent runs these sub-agents in sequence. All agent output should be stored in `/jobs/*/analysis/`. The pipeline runs in four phases:

**Phase 1: Critical Quality Gates** (must pass before proceeding)
| # | Sub-agent | What it does |
|---|-----------|-------------|
| 1 | Fact Checker | Verifies all claims against your profile (`/data/tyson/profile.md`). If it flags issues, the pipeline halts for corrections. |
| 2 | Think Like Tyson | Ensures the document reflects your authentic voice and personal guidelines. If misaligned, the pipeline halts for revision. |

**Phase 2: Functional Improvements** (only if Phase 1 passes)
| # | Sub-agent | What it does |
|---|-----------|-------------|
| 3 | ATS Analyzer | Checks keyword coverage and format compatibility |
| 4 | Keyword Gap Agent | Finds semantic mismatches between your profile and the JD |
| 5 | Impact Quantifier | Rewrites weak bullets into quantified achievements |
| 6 | Tone Optimizer | Aligns writing style with the role's seniority and company culture |

**Phase 3: Final Arbitration** (only if Phases 1 & 2 complete)
| # | Sub-agent | What it does |
|---|-----------|-------------|
| 7 | Conflict Resolver | Resolves contradictions between agents and recommends final changes (does not modify files directly) |

**Phase 4: Change Composition** (only if Phase 3 complete)
| # | Sub-agent | What it does |
|---|-----------|-------------|
| 8 | Change Composer | Drafts proposed CV and cover letter with all recommended changes applied; generates PDF for visual review |

### Step 4 — Review Proposed Changes

The Change Composer generates proposed files in the `analysis/` folder:

| File | Purpose |
|------|---------|
| `analysis/proposed-cv.typ` | Full CV with recommended changes applied |
| `analysis/proposed-cv.pdf` | Compiled PDF of proposed CV for visual review |
| `analysis/proposed-cover-letter.md` | Full cover letter with recommended changes applied |
| `analysis/change-summary.md` | Clear summary of what changed and why |

Review these proposed files and decide:
- **Approve** — Apply all changes to actual `cv.typ` and `cover-letter.md`
- **Request modifications** — Ask for specific iterations before applying
- **Reject** — Keep current versions unchanged

### Step 5 — Compile and Submit

Once you approve the changes:

```bash
cd "jobs/<Company Name> - <Job Title> - <City>, <Country>"
# Copy approved changes from proposed files
cp analysis/proposed-cv.typ cv.typ
cp analysis/proposed-cover-letter.md cover-letter.md
# Recompile the final PDF
typst compile cv.typ cv.pdf
```

---

## Interview preparation

Once you have an interview scheduled, ask the agent:

> "Generate interview prep for [job folder name]"

The agent will create `interview-prep.md` inside the job folder with:
- Role-specific likely questions.
- Suggested answers based on your profile.
- Questions to ask the interviewer.
- Research notes about the company.

---

## Content rules

All generated content must comply with the rules in `constraints/content-guidelines.md`:

1. **Factual accuracy** — every claim must come from `data/tyson/`.
2. **Concise, simple language** — short sentences, active voice, no filler.
3. **No AI-sounding language** — no "leverage", "delve", "synergy", or similar; see the full banned list.

---

## Updating your profile

Whenever your situation changes (new job, new skill, new certification), update `data/tyson/profile.md`. All future job applications will automatically reflect the change.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `typst: command not found` | See the Installation section in `Typst.md` |
| CV PDF looks wrong | Run `typst watch cv.typ cv.pdf` and check for errors in the terminal |
| Agent invents facts | Remind the agent to follow `constraints/content-guidelines.md` Rule 1 |
| Missing keywords in CV | Re-run the ATS Analyzer sub-agent with the updated draft |
