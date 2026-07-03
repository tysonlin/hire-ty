---
name: application-pdf
description: Combine a job application's CV (cv.tex) and cover letter (cover-letter.md) into a single application.pdf using LaTeX, with the CV on page 1 and the cover letter on page 2. Use this whenever Tyson asks to combine, merge, or bundle a CV and cover letter into one PDF, or asks for an "application.pdf" for a job folder under jobs/.
---

# Application PDF

Produces a single `application.pdf` by embedding `cv.tex` content and `cover-letter.md` content into one LaTeX source file (`application.tex`), compiling to a 2-page PDF with `xelatex`.

## When to use

- Tyson asks to "combine CV and cover letter into one PDF"
- Tyson asks to create `application.pdf` for a job
- Tyson asks to "bundle" or "merge" the application documents

If Tyson doesn't name the job folder, ask which folder under `jobs/` to use (naming convention: `jobs/<Company Name> - <Job Title> - <City>, <Country>/`).

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
- Escape special characters: escape `&`, `%`, `#`, `_` as `\&`, `\%`, `\#`, `\_`
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
