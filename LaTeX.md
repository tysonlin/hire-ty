# LaTeX CV Generation

This document explains how to use LaTeX (compiled with `xelatex`) to produce the tailored CV
for each job application. LaTeX replaces the previous Typst workflow: it compiles inside the
Claude sandbox (where Typst cannot be installed) and on your Mac.

---

## Why LaTeX

- `xelatex` is preinstalled in the Claude sandbox, so the agent can compile `cv.pdf` directly
  every run. Typst could not be installed there (the sandbox blocks all package downloads and is
  wiped between sessions).
- Produces clean, ATS-friendly, one-page PDFs.
- A single source file, `cv.tex`, is the source of truth. Edit it and recompile.

---

## Installation (your Mac)

The sandbox already has `xelatex`. To compile locally on macOS, install MacTeX (or the smaller
BasicTeX):

```bash
# Full distribution (large, ~5 GB, includes everything)
brew install --cask mactex

# OR minimal distribution, then add the few packages we use
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install fontspec geometry enumitem titlesec
```

Verify:

```bash
xelatex --version
```

### Fonts

The template prefers **Linux Libertine O** (to match the original CV look) and automatically
falls back to **TeX Gyre Termes** (a Times-like serif) when Libertine is not installed. This is
handled by `\IfFontExistsTF`, so the same `cv.tex` compiles in both environments with no edits:

```latex
\IfFontExistsTF{Linux Libertine O}
  {\setmainfont{Linux Libertine O}}
  {\setmainfont{TeX Gyre Termes}}
```

Environment notes:

- **This Mac** has Linux Libertine O installed, so it uses Libertine.
- **The Claude sandbox** has TeX Gyre Termes but not Libertine, so it uses Termes.
- **BasicTeX** does not ship TeX Gyre Termes by default. To have the fallback available locally
  (full parity with the sandbox), install it:

  ```bash
  sudo tlmgr install tex-gyre
  # or, for the full standard font set:
  sudo tlmgr install collection-fontsrecommended
  # verify:
  kpsewhich texgyretermes-regular.otf
  ```

- If you want pixel-identical output everywhere, install **both** fonts in both places: add
  Linux Libertine via Font Book on the Mac, and `tex-gyre` via tlmgr. With the conditional above,
  whichever is present wins, Libertine first.

---

## Compiling the CV

From the job folder:

```bash
cd "jobs/<Company Name> - <Job Title> - <City>, <Country>"
xelatex -interaction=nonstopmode cv.tex
```

This produces `cv.pdf` in the same folder. `xelatex` also writes `cv.aux`, `cv.log`, and
`cv.out` — these are build artifacts and can be deleted or git-ignored.

To keep the folder clean, compile to a temp directory and copy only the PDF back:

```bash
xelatex -interaction=nonstopmode -output-directory=/tmp/cvbuild cv.tex
cp /tmp/cvbuild/cv.pdf cv.pdf
```

### Check the CV is one page

```bash
xelatex -interaction=nonstopmode cv.tex >/dev/null 2>&1
pdfinfo cv.pdf | grep Pages
```

`Pages: 1` is the target. If it overflows, see the one-page trim notes below.

---

## CV template

Each job folder contains a self-contained `cv.tex`. It needs only standard packages
(`fontspec`, `geometry`, `enumitem`, `titlesec`, `xcolor`, `hyperref`) that ship with MacTeX and
the sandbox. No external template download is required.

```latex
% !TEX program = xelatex
\documentclass[10pt]{article}
\usepackage[a4paper,top=0.7cm,bottom=0.7cm,left=1.3cm,right=1.3cm]{geometry}
\usepackage{fontspec}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{hyperref}
\hypersetup{hidelinks}

% Font: prefer Linux Libertine O (Mac); fall back to TeX Gyre Termes (sandbox / BasicTeX).
% Same file compiles in both environments without edits.
\IfFontExistsTF{Linux Libertine O}
  {\setmainfont{Linux Libertine O}}
  {\setmainfont{TeX Gyre Termes}}

\setlength{\parindent}{0pt}
\linespread{0.98}
\pagestyle{empty}

% Section heading with full-width rule under it
\titleformat{\section}{\large\bfseries}{}{0em}{}[\vspace{-0.6em}\rule{\linewidth}{0.4pt}\vspace{-0.2em}]
\titlespacing{\section}{0pt}{6pt}{2pt}
% Role / project sub-heading
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}
\titlespacing{\subsection}{0pt}{4pt}{0pt}
\setlist[itemize]{leftmargin=1.2em,topsep=1pt,itemsep=0.5pt,parsep=0pt}

\begin{document}
\fontsize{9.5pt}{11.5pt}\selectfont

% ---------- Header ----------
\begin{center}
{\fontsize{14pt}{16pt}\selectfont \textbf{<Full Name>}}\\[2pt]
{\fontsize{8pt}{9pt}\selectfont <Phone> \ \textbar\ <Email> \ \textbar\ <LinkedIn> \ \textbar\ <GitHub>}
\end{center}
\vspace{-2pt}
\rule{\linewidth}{1pt}

\section*{Professional Summary}
<Two to three sentence summary tailored to the role.>

\section*{Core Skills}
\textbf{<Category>:} <Skill 1>, <Skill 2>, <Skill 3>\\
\textbf{<Category>:} <Skill 1>, <Skill 2>, <Skill 3>

\section*{Work Experience}

\subsection*{<Job Title> --- <Company>}
\textit{<Start> -- <End>} \ \textbar\ <City>, <Country> \ \textbar\ \textit{Internal Role:} <Internal Title>
\begin{itemize}
\item <Achievement or responsibility with measurable impact.>
\item <Achievement or responsibility with measurable impact.>
\end{itemize}

\subsection*{Earlier Experience (<Year>--<Year>)}
\textbf{<Company>} (<Year>--<Year>, <City>): \textit{<Role>}, <brief> \ \textbar\ \textbf{<Company>} (<Year>, <City>): \textit{<Role>}

\section*{Key Projects}

\subsection*{<Project Name> \textnormal{(\textit{<Year>--<Year>})}}
<Two to three sentence description of scope, approach, and impact.>

\section*{Education \& Certifications}
<Degree>, <Institution> (<City>, <Country>), <Years> \ \textbar\ <Degree>, <Institution> (<City>, <Country>), <Years>

\end{document}
```

### Syntax quick reference

| LaTeX | Output |
|-------|--------|
| `\section*{Heading}` | Section heading with rule (h2) |
| `\subsection*{Sub-heading}` | Role / project heading (h3) |
| `\textbf{text}` | **Bold** |
| `\textit{text}` | *Italic* |
| `\begin{itemize}\item ...\end{itemize}` | Bullet list |
| `\\` | Line break within a paragraph |
| `\ \textbar\ ` | Separator " \| " with even spacing |
| `\%` | Literal `%` |
| `\#` | Literal `#` (e.g. `C\#`) |
| `\&` | Literal `&` (e.g. `Data \& Messaging`) |
| `--` / `---` | En-dash / em-dash |

Note: the section order (Header → Summary → Core Skills → Work Experience → Earlier Experience →
Key Projects → Education) must stay stable; ATS systems expect standard ordering. Do not reorder
without re-running the ATS Analyzer sub-agent.

---

## VS Code / LaTeX Workshop

LaTeX Workshop's default recipe uses `latexmk` + pdfLaTeX. That fails here for two reasons:
BasicTeX does not install `latexmk` (`spawn latexmk ENOENT`), and our template needs `xelatex`
(the `fontspec` package only works under XeTeX/LuaTeX, not pdfLaTeX).

The repo ships a workspace config at `.vscode/settings.json` that points LaTeX Workshop at
`xelatex` directly and auto-cleans build artifacts. Each `cv.tex` also starts with the magic
comment `% !TEX program = xelatex`, so other editors (TeXShop, etc.) pick XeTeX too. Reload the
VS Code window after opening the repo so the settings take effect, then save `cv.tex` to build.

If you prefer `latexmk` (auto multi-pass), install it and use a xelatex recipe instead:

```bash
sudo tlmgr install latexmk
```

```json
// .vscode/settings.json
"latex-workshop.latex.tools": [
  { "name": "xelatexmk", "command": "latexmk",
    "args": ["-xelatex","-synctex=1","-interaction=nonstopmode","-file-line-error","%DOC%"] }
],
"latex-workshop.latex.recipes": [ { "name": "xelatexmk", "tools": ["xelatexmk"] } ],
"latex-workshop.latex.recipe.default": "xelatexmk"
```

Our CV has no cross-references or bibliography, so a single `xelatex` pass is enough; `latexmk`
is optional.

---

## One-page trim levers

If the CV overflows to a second page, tighten in this order (small steps, recompile each time):

1. Body font: `\fontsize{9.5pt}{11.5pt}` → `9pt`/`11pt`.
2. Line spacing: `\linespread{0.98}` → `0.95`.
3. List spacing: lower `itemsep` / `topsep` in the `\setlist` line.
4. Page margins: reduce in the `geometry` line (do not go below ~0.6cm).
5. Content: cut the weakest bullet from the oldest roles.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `xelatex: command not found` | Install MacTeX/BasicTeX (see Installation) |
| `The font "..." cannot be found` | Install the font, or switch `\setmainfont` to `TeX Gyre Termes` |
| `! LaTeX Error: File 'fontspec.sty' not found` | `sudo tlmgr install fontspec geometry enumitem titlesec` |
| PDF overflows one page | Apply the trim levers above |
| Stray `&`, `%`, `#`, `_` errors | Escape them: `\&`, `\%`, `\#`, `\_` |
