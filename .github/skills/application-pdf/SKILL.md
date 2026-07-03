---
name: application-pdf
description: "Combine a job application's CV (cv.tex) and cover letter (cover-letter.md) into a single application.pdf using LaTeX. CV on page 1, cover letter on page 2. Use when asked to combine, merge, or bundle CV and cover letter into one PDF, or when creating application.pdf for a job folder."
argument-hint: "Path to job folder, e.g. jobs/Acme - Engineer - Sydney, Australia"
---

# application-pdf

Produces a single `application.pdf` by embedding `cv.tex` content and `cover-letter.md` content into one LaTeX source file (`application.tex`), compiling to a 2-page PDF with `xelatex`.

## When to Use

- User asks to "combine CV and cover letter into one PDF"
- User asks to create `application.pdf` for a job
- User asks to "bundle" or "merge" the application documents

## Procedure

### 1. Read source files

Read the current `cv.tex` and `cover-letter.md` from the job folder.

### 2. Create `application.tex`

Create `application.tex` in the job folder. Reuse the CV preamble, put the CV body on page 1,
then `\newpage` into a wider-margin cover-letter page:

```latex
% ── Preamble: copy verbatim from cv.tex (documentclass + all \usepackage + font + \titleformat) ──

\begin{document}

% ── Page 1: CV ──────────────────────────────────────────────────────────────
\fontsize{9.5pt}{11.5pt}\selectfont
% Paste the CV body from cv.tex here (header, \section* blocks, etc.)

% ── Page 2: Cover Letter ────────────────────────────────────────────────────
\newpage
\newgeometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm}
\fontsize{11pt}{15pt}\selectfont
\setlength{\parskip}{0.8em}
\setlength{\parindent}{0pt}

% Cover letter body: one blank line between paragraphs.
% Sign-off lines use \\ for hard line breaks.

\restoregeometry
\end{document}
```

Key rules for the cover letter page:
- Convert markdown to LaTeX (no `**bold**`, no `#` headings)
- Escape special characters: `\@` is not needed in LaTeX, but escape `&`, `%`, `#`, `_` as `\&`, `\%`, `\#`, `\_`
- Use `\\` at end of line for hard line breaks (e.g. in the sign-off block)
- Separate paragraphs with a blank line (with `\parskip` set, no manual spacing needed)
- `\newgeometry` / `\restoregeometry` requires the `geometry` package (already loaded in the CV preamble)

### 3. Compile

```bash
cd "<job-folder>"
xelatex -interaction=nonstopmode application.tex
```

### 4. Verify

Confirm `application.pdf` exists and is 2 pages:

```bash
pdfinfo application.pdf | grep Pages
```
