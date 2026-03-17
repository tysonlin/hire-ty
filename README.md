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
│   ├── ats-analyzer.md
│   ├── keyword-gap-agent.md
│   ├── impact-quantifier.md
│   ├── tone-optimizer.md
│   └── conflict-resolver.md
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

The agent runs these sub-agents in order, then the Conflict Resolver finalises the output. The output for these subagents should be stored at each job folder under `/jobs/*/analysis/`:

| # | Sub-agent | What it does |
|---|-----------|-------------|
| 1 | ATS Analyzer | Checks keyword coverage and format compatibility |
| 2 | Keyword Gap Agent | Finds semantic mismatches between your profile and the JD |
| 3 | Impact Quantifier | Rewrites weak bullets into quantified achievements |
| 4 | Tone Optimizer | Aligns writing style with the role's seniority and company culture |
| 5 | Conflict Resolver | Resolves any contradictions and produces the final documents |

### Step 4 — Compile the CV

```bash
cd "jobs/<Company Name> - <Job Title> - <City>, <Country>"
typst compile cv.typ cv.pdf
```

See `Typst.md` for full details including watch mode and the VS Code extension.

### Step 5 — Review and send

- Open `cv.pdf` and `cover-letter.md`.
- Check for any `[TODO: ...]` placeholders and fill them in.
- Send!

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
