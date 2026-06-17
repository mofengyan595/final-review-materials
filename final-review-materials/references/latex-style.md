# LaTeX Style

Use XeLaTeX with `ctex` for Chinese review handouts. Prefer clean, readable academic notes over decorative layouts. The page should feel easy to keep reading: clear headings, generous but not wasteful spacing, restrained color, and boxes only where they improve study.

## Base Packages

Use these packages unless the project has a stronger template:

- `ctex`
- `geometry`
- `amsmath`, `amssymb`, `mathtools`
- `graphicx`
- `booktabs`, `longtable`, `array`, `tabularx`
- `enumitem`
- `xcolor`
- `tcolorbox`
- `hyperref`
- `tikz` only when diagrams are simple enough to verify

## Boxes

Use distinct boxes for original questions, answers, warnings, and exam-day quick notes. Keep question stems visually separate from analysis and answers. Do not over-box normal theory explanations, memorization entries, or every minor note.

Recommended command names:

- `questionbox` for original stems.
- `answerbox` for formal answers.
- `notebox` for important notes.
- `warningbox` for mistakes or uncertain source issues.
- `\examfield{...}` for weak labels such as `考查知识点`, `题目解析`, and `易错点`.

Avoid bracket priority tags in memorization entries unless the user asks for them. Use typography and ordering, not labels like `[核心]`, to keep背诵 sections clean.

## Figures

- Store cropped figures under `figures/`.
- Use descriptive ASCII-safe file names such as `ch03-pipeline-hazard.png`.
- Captions must explain what the figure is and why it matters.
- Do not use a figure if its key labels are unreadable after scaling.
- For cropped images, inspect the rendered PDF page, not just the source image. Confirm no axes, arrows, pin names, legends, waveforms, formula labels, or explanatory text are clipped after scaling.
- If a diagram is redrawn with TikZ, compare it against the source and check arrow direction, labels, nodes, axes, timing, and formula placement.

## Tables

- Use `booktabs` for normal tables.
- Use `tabularx` for text-heavy comparison tables.
- Use `longtable` for multi-page tables.
- Split or rewrite wide tables; do not accept overfull boxes or overlapping text.
- Keep table cells concise. Put long explanations in paragraphs below the table.

## Formulas

- Use display math for important formulas.
- Always explain symbol meanings and applicable conditions.
- Add a small example when the formula is likely to be used in calculations.
- Keep similar formulas close together and compare their conditions.

## Compilation

Compile with XeLaTeX. Run enough passes for references and table of contents. Then inspect:

- Fatal errors.
- Undefined references or citations.
- Missing characters or font warnings.
- Overfull boxes.
- Figure cropping and scaling.
- Table overflow.
- Text overlap in boxes and diagrams.

Use `scripts/audit_latex_build.py` as a log scanner, but do not treat it as a replacement for visual inspection.

## Large Projects

For long courses, split content into `sections/chXX-title.tex` files and include them from `main.tex`. Keep lecture examples inside the chapter file that explains the corresponding concept. Keep assignments, past exams, and prediction questions in their own later section files. Create a lab section file only when lab materials or exam scope explicitly require it.

Use `extracted/` notes as source anchors while writing. Do not paste OCR dumps directly into the final LaTeX; rewrite them into polished explanations and keep uncertain recognition issues marked. Do not include default source catalogs, `资料说明`, version/change notes, or standalone symbol-convention pages in the final PDF.
