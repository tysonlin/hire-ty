---
name: trim-cv-to-one-page
description: "Trim a job application CV (cv.typ) to fit exactly one page by adjusting font size, line spacing, and content density. Use when asked to shrink, trim, fit to one page, or reduce a CV that is overflowing onto a second page."
argument-hint: "Path to job folder, e.g. jobs/Acme - Engineer - Sydney, Australia"
---

# trim-cv-to-one-page

Trims a Typst CV (`cv.typ`) to fit on a single page without sacrificing key content. Works by progressively reducing layout parameters and tightening content.

## When to Use

- User says the CV is running onto 2 pages
- User asks to "trim to one page", "make it fit", or "shrink the CV"
- After compiling, the PDF page count is 2

## Page Count Verification

After any compile, verify page count with:

```bash
cd "<job-folder>"
typst compile cv.typ cv.pdf && python3 -c "
import re
with open('cv.pdf', 'rb') as f: data = f.read()
print('Pages:', len(re.findall(b'/Type /Page[^s]', data)))
"
```

Target: `Pages: 1`

---

## Procedure

### Step 1: Check current layout settings

Read the top of `cv.typ` and note:
- `#set page(margin: ...)` values
- `#set text(... size: ...)` value
- Whether `#set par(leading: ...)` is set

### Step 2: Apply layout adjustments (in order)

Apply these in sequence, recompiling and checking page count after each:

#### 2a. Tighten margins (if not already tight)

Standard tight margin for a one-page CV:

```typst
#set page(margin: (top: 0.7cm, bottom: 0.7cm, left: 1.3cm, right: 1.3cm))
```

#### 2b. Reduce font size

Start at 10pt. Reduce by 0.25pt steps until the CV fits:

| Step | Font size |
|------|-----------|
| 1    | 9.8pt     |
| 2    | 9.5pt     |
| 3    | 9.25pt    |

Do not go below **9pt** — readability degrades significantly.

```typst
#set text(font: "Linux Libertine O", size: 9.5pt)
```

#### 2c. Reduce line spacing (if still overflowing after font reduction)

Add or tighten `#set par(leading: ...)` directly after the `#set text(...)` line:

```typst
#set par(leading: 0.60em)
```

Default Typst leading is ~0.65em. Use 0.60em as the standard trim value. Do not go below **0.55em**.

### Step 3: Tighten content (if layout changes are insufficient)

If layout-only changes are not enough:

1. **Shorten bullet points** — cut redundant phrases; target ≤2 lines per bullet
2. **Condense older roles** — collapse pre-2018 experience into a single compact line:
   ```
   == Additional Experience
   *Role (Years):* Short summary | *Role (Years):* Short summary
   ```
3. **Trim the Professional Summary** — reduce to 2–3 sentences if longer
4. **Shorten Key Projects** — reduce to 1–2 sentences per project; or remove the section entirely if the content is already covered in Work Experience

### Step 4: Final compile and verify

```bash
typst compile cv.typ cv.pdf && python3 -c "
import re
with open('cv.pdf', 'rb') as f: data = f.read()
print('Pages:', len(re.findall(b'/Type /Page[^s]', data)))
"
```

Confirm output: `Pages: 1`
