# /jobs — Job Applications

Each job application lives in its own sub-folder under this directory.

## Folder naming convention

```
<Company Name> - <Job Title> - <City>, <Country>
```

**Examples:**
```
Acme Corp - Senior Software Engineer - Sydney, Australia
Globex - Product Manager - Remote, Global
```

## Folder contents

When a new job description is provided to the agent, it will create the folder and populate:

| File | Description |
|------|-------------|
| `job-description.md` | Summarised and structured version of the original job description |
| `cv.typ` | Typst source for the tailored CV (see `/Typst.md` for build instructions) |
| `cv.pdf` | Compiled CV (generated from `cv.typ`) |
| `cover-letter.md` | Tailored cover letter in email format |
| `interview-prep.md` | Interview preparation notes (created once an interview is scheduled) |

## Workflow

1. Provide the agent with a job description URL or paste the full job description.
2. The agent creates the job folder and `job-description.md`.
3. The agent runs all sub-agents (see `/subagents/`) and generates `cv.typ` and `cover-letter.md`.
4. Compile the CV to PDF using the instructions in `/Typst.md`.
5. If you progress to an interview, ask the agent to generate `interview-prep.md`.
