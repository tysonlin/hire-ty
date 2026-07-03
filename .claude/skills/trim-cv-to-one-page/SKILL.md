---
name: trim-cv-to-one-page
description: Trim a job application CV (cv.tex) to fit exactly one page by adjusting font size, line spacing, and content density. Use this whenever Tyson says a CV is overflowing onto a second page, or asks to shrink, trim, or "make it fit" a CV to one page.
---

# Trim CV to One Page

Trims a LaTeX CV (`cv.tex`) to fit on a single page without sacrificing key content. Works by progressively reducing layout parameters and tightening content.

## When to use

- Tyson says the CV is running onto 2 pages
- Tyson asks to "trim to one page", "make it fit", or "shrink the CV"
- After compiling, the PDF page count is 2

If Tyson doesn't name the job folder, ask which folder under `jobs/` to use (naming convention: `jobs/<Company Name> - <Job Title> - <City>, <Country>/`).

## Page count verification

After any compile, verify page count with:

```bash
cd "<job-folder>"
xelatex -interaction=nonstopmode cv.tex >/dev/null 2>&1 && pdfinfo cv.pdf | grep Pages
```

Target: `Pages: 1`

(If `pdfinfo` is unavailable, count pages with:
`python3 -c "import re;d=open('cv.pdf','rb').read();print('Pages:',len(re.findall(b'/Type\\s*/Page[^s]',d)))"`)

---

## Procedure

### Step 1: Check current layout settings

Read the top of `cv.tex` and note:
- the `geometry` margin values (`\usepackage[...]{geometry}`)
- the body font size (`\fontsize{9.5pt}{11.5pt}\selectfont`)
- the line spacing (`\linespread{...}`)
- the list spacing (`\setlist[itemize]{...}`)

### Step 2: Apply layout adjustments (in order)

Apply these in sequence, recompiling and checking page count after each:

#### 2a. Tighten margins (if not already tight)

Standard tight margin for a one-page CV:

```latex
\usepackage[a4paper,top=0.7cm,bottom=0.7cm,left=1.3cm,right=1.3cm]{geometry}
```

#### 2b. Reduce body font size

Start at 9.5pt. Reduce in small steps until the CV fits:

| Step | Font size (`\fontsize{X}{Y}`) |
|------|-------------------------------|
| 1    | `9.5pt`/`11.5pt`              |
| 2    | `9.25pt`/`11pt`              |
| 3    | `9pt`/`11pt`                 |

Do not go below **9pt** — readability degrades significantly.

```latex
\fontsize{9.5pt}{11.5pt}\selectfont
```

#### 2c. Reduce line spacing (if still overflowing after font reduction)

Tighten `\linespread{...}` near the top of the preamble:

```latex
\linespread{0.95}
```

Use 0.98 as the default and 0.95 as the standard trim value. Do not go below **0.92**.

#### 2d. Tighten list spacing

Lower `itemsep` / `topsep` in the `\setlist` line:

```latex
\setlist[itemize]{leftmargin=1.2em,topsep=1pt,itemsep=0.3pt,parsep=0pt}
```

### Step 3: Tighten content (if layout changes are insufficient)

If layout-only changes are not enough:

1. **Shorten bullet points** — cut redundant phrases; target ≤2 lines per bullet
2. **Condense older roles** — collapse pre-2018 experience into a single compact line:
   ```latex
   \subsection*{Earlier Experience (<Year>--<Year>)}
   \textbf{<Company>} (<Years>): \textit{<Role>}, short summary \ \textbar\ \textbf{<Company>} (<Years>): \textit{<Role>}
   ```
3. **Trim the Professional Summary** — reduce to 2–3 sentences if longer
4. **Shorten Key Projects** — reduce to 1–2 sentences per project; or remove the section entirely if the content is already covered in Work Experience

### Step 4: Final compile and verify

```bash
xelatex -interaction=nonstopmode cv.tex >/dev/null 2>&1 && pdfinfo cv.pdf | grep Pages
```

Confirm output: `Pages: 1`
