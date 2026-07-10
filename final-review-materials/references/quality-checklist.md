# Quality Checklist

Run this checklist before claiming the review handout is complete.

## Completeness

- All uploaded source files were read or explicitly marked unreadable.
- `coverage/source-inventory.csv` contains one row per source with a valid coverage mode, unit count where required, read status, and example-scan status.
- Every page or slide in teacher theory slides, lab slides, and official exam-scope materials has exactly one classified row in `coverage/source-coverage.csv`.
- Every countable unit in another source marked `page` or `item` is present in the coverage matrix.
- Every substantive coverage row maps to a knowledge-point ID and final output location; every merged row points to the retained location.
- Title, divider, decoration, duplicate, or empty pages are explicitly classified instead of silently omitted.
- `coverage/example-catalog.csv` includes every lecture example, demonstration problem, in-slide exercise, and question-like prompt found during text and visual inspection.
- Every mapped lecture example preserves source location, stem completeness, necessary media, answer provenance, knowledge-point ID, and final output location.
- `scripts/audit_source_coverage.py <review-project> --strict` passes before the handout is called complete.
- Each nontrivial source has an `extracted/` note with OCR text, figure index, page/slide provenance, and uncertainty notes.
- All theory chapters in teacher materials are covered.
- A standalone lab section is present only when lab materials exist or the exam scope explicitly says lab content/principles will be tested.
- If the lab gate is met, all relevant lab topics are covered; if not, no generic lab chapter was created.
- The complete review handout remains the main artifact;专项训练,背诵版, and临考速记 do not replace chapter explanations unless the user requested a specialized-only output.
- If the user provided exam question types, the practice and prediction sections match those exact types.
- Textbook content is used to complete definitions, background, derivations, and chapter logic.
- Assignment questions are used to reinforce knowledge points and mistake patterns.
- Past exams are preserved with original stems and used for question-style analysis.
- Senior-note-only content is marked as supplementary, not treated as confirmed exam scope.
- The handout can replace the slides and notes for a student who missed lectures.
- The handout can teach a zero-base student without requiring unexplained terminology or hidden intermediate reasoning from the slides.
- Large courses were split by chapter instead of compressed into a short outline.

## OCR And Source Fidelity

- Scanned PDFs, slide images, embedded images, figures, and question images were OCRed or inspected.
- The OCR toolchain used for PDFs, PPT-rendered pages, and images is recorded in logs or extraction notes.
- Uncertain OCR terms, formulas, diagrams, labels, and missing answers are marked `需人工核对`.
- Conflicting sources are resolved according to source priority.
- Important claims have nearby source hints when useful.

## Writing Quality

- Explanations are detailed, beginner-friendly, and not just bullet outlines.
- Technical terms and abbreviations are explained at first use before they are used to define other new concepts.
- Each nontrivial knowledge point includes the applicable prerequisites, motivating problem, intuition, formal definition, mechanism or derivation, worked example, mistakes, self-check, and exam wording.
- Formula explanations include symbol meanings, units when applicable, assumptions, valid conditions, intermediate reasoning, and a worked use.
- Figures, tables, waveforms, circuits, and code fragments have nearby guidance explaining what to observe and why it matters.
- Mnemonics, summaries, and comparison tables supplement rather than replace full teaching prose.
- Teaching style is textbook-like: concept explanation, example, exam hint, mistake, and summary appear in context.
- Repeated concepts are merged into the most relevant chapter.
- There are no draft/process phrases such as `根据用户要求`, `本版`, `上一版`, `自绘图`, `这里先`.
- There are no default final `资料说明`, `资料识别与目录梳理`, source catalogs, version/change notes, or standalone symbol-convention pages unless explicitly requested.
- Theory, formula, comparison, assignment, past-exam, prediction, and sprint sections are clearly separated; lab is separated only when applicable.
- Final predictions are based primarily on past exams, not unsupported notes.
- Exam-day quick review is compact and course-specific, not a generic forced format.

## Questions

- Every important assignment or exam question keeps the original stem.
- Lecture-example discovery checked rendered pages and embedded images, not only OCR keywords such as `例题`.
- Multi-slide examples keep their stem, intermediate steps, and source-provided solution together.
- Lecture examples are placed near the related knowledge point, not only in a detached question bank.
- Source-provided answers and agent-derived solutions are labeled distinctly; derived work is never presented as the teacher's answer.
- Calculation examples show known quantities, target, selected rule, substitution, intermediate steps, units, result, and a sanity check when applicable.
- Assignments, past exams, and prediction questions are separated by source type.
- Predictions and same-type exercises follow the exam question types provided by the user or inferred from sample/past exams.
- Answer-style advice is inferred from teacher, homework, sample-exam, or past-exam answers; no universal fixed answer template is invented.
- If 名词解释 or 术语解释 is confirmed, a clean集中背诵版 or separated section exists.
- Memorization entries do not include bracket tags such as `[原题]`, `[核心]`, `[高频]`, or `[大写缩写]` unless the user requested labels.
- Original stem, knowledge point, analysis, formal answer, and mistakes are visually separate.
- Formal answers are highlighted.
- Multiple-choice options are not squeezed into one paragraph.
- Question images and answer images are preserved or redrawn correctly.
- Uncertain answers are marked `参考答案需人工核对`.

## Figures And Tables

- No unnecessary whole-slide screenshots.
- Cropped figures include all labels, arrows, axes, legends, pins, waveforms, and key text.
- Cropped figures were checked on the rendered PDF page at final scale.
- Complex diagrams use original crops unless a faithful redraw is verified.
- Simple diagrams redrawn with TikZ are checked against the source.
- Tables do not overflow, overlap, or become unreadable.

## LaTeX Build

- XeLaTeX compiles successfully.
- References and table of contents are stable after repeated passes.
- Logs were checked for fatal errors, undefined references, missing characters, and overfull boxes.
- Rendered PDF pages were inspected for text overlap, bad page breaks, clipped images, and broken boxes.

## Completion Gate

- Source coverage and lecture-example completeness were checked independently from LaTeX build quality.
- No required unit is absent from the coverage matrix.
- No example remains unmapped.
- No `needs-review`, `partial`, `unreadable`, missing-answer, or conflicting-answer item remains when the handout is called complete; unavoidable source damage is listed as `需人工核对` and the delivery is labeled incomplete or partially verified.
- Page count, word count, or the presence of chapter headings was not used as a substitute for coverage evidence.
