# Quality Checklist

Run this checklist before claiming the review handout is complete.

## Completeness

- All uploaded source files were read or explicitly marked unreadable.
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
- Large courses were split by chapter instead of compressed into a short outline.

## OCR And Source Fidelity

- Scanned PDFs, slide images, embedded images, figures, and question images were OCRed or inspected.
- The OCR toolchain used for PDFs, PPT-rendered pages, and images is recorded in logs or extraction notes.
- Uncertain OCR terms, formulas, diagrams, labels, and missing answers are marked `需人工核对`.
- Conflicting sources are resolved according to source priority.
- Important claims have nearby source hints when useful.

## Writing Quality

- Explanations are detailed, beginner-friendly, and not just bullet outlines.
- Teaching style is textbook-like: concept explanation, example, exam hint, mistake, and summary appear in context.
- Repeated concepts are merged into the most relevant chapter.
- There are no draft/process phrases such as `根据用户要求`, `本版`, `上一版`, `自绘图`, `这里先`.
- There are no default final `资料说明`, `资料识别与目录梳理`, source catalogs, version/change notes, or standalone symbol-convention pages unless explicitly requested.
- Theory, formula, comparison, assignment, past-exam, prediction, and sprint sections are clearly separated; lab is separated only when applicable.
- Final predictions are based primarily on past exams, not unsupported notes.
- Exam-day quick review is compact and course-specific, not a generic forced format.

## Questions

- Every important assignment or exam question keeps the original stem.
- Lecture examples are placed near the related knowledge point, not only in a detached question bank.
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
