---
name: application-pdf
description: "Combine a job application's CV (cv.typ) and cover letter (cover-letter.md) into a single application.pdf using Typst. CV on page 1, cover letter on page 2. Use when asked to combine, merge, or bundle CV and cover letter into one PDF, or when creating application.pdf for a job folder."
argument-hint: "Path to job folder, e.g. jobs/Acme - Engineer - Sydney, Australia"
---

# application-pdf

Produces a single `application.pdf` by embedding `cv.typ` content and `cover-letter.md` content into one Typst source file (`application.typ`), compiling to a 2-page PDF.

## When to Use

- User asks to "combine CV and cover letter into one PDF"
- User asks to create `application.pdf` for a job
- User asks to "bundle" or "merge" the application documents

## Procedure

### 1. Read source files

Read the current `cv.typ` and `cover-letter.md` from the job folder.

### 2. Create `application.typ`

Create `application.typ` in the job folder using this structure:

```typst
// ── Page 1: CV ────────────────────────────────────────────────────────────────

// Paste cv.typ content here verbatim (all #set rules, header, sections)

// ── Page 2: Cover Letter ──────────────────────────────────────────────────────

#pagebreak()

#set page(margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm))
#set text(size: 11pt)
#set par(leading: 0.75em, spacing: 1.2em)

// Cover letter content in Typst markup:
// - Contact line: email \ and phone \ using backslash line breaks
// - #v(1em) spacer before salutation
// - Paragraphs separated by blank lines
// - #v(1em) before sign-off block
// - Sign-off lines use \ for line breaks
```

Key rules for the cover letter page:
- Convert markdown to Typst markup (no `**bold**`, no `#` headings)
- Escape `@` in email addresses as `\@`
- Use `\` (backslash) at end of line for hard line breaks
- Use `#v(1em)` for vertical spacing between blocks

### 3. Compile

```bash
cd "<job-folder>"
typst compile application.typ application.pdf
```

### 4. Verify

Confirm exit code 0 and that `application.pdf` exists in the job folder.
