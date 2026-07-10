---
name: final-review-materials
description: Use when creating zero-base, course-replacing Chinese LaTeX exam-review handouts from course PDFs, PPTs, textbooks, assignments, notes, past exams, exam scopes, OCR-heavy scanned files, or image-based lecture content, especially when slide-complete coverage, full lecture-example extraction, or matching exam-type专项训练 matters.
---

# Final Review Materials

## Overview

Create complete, course-replacing LaTeX review handouts from mixed course materials. Treat completeness, beginner readability, and source fidelity as higher priority than brevity: the final document should teach a zero-base student who missed the lectures, not merely list key points. When the user provides exam question types, add matching exam-type专项训练 as a supplement to the full handout.

## Core Rules

- Read real source files before judging content, structure, or missing information.
- Treat slide coverage as evidence, not an impression. Classify every page or slide of teacher theory slides, lab slides, and official exam-scope materials in the internal coverage matrix before claiming completeness.
- Treat lecture examples as first-class source content. Catalog every example, demonstration problem, in-slide exercise, question-like prompt, and multi-slide worked solution before drafting chapters; preserve its source and answer provenance.
- Teach from zero prerequisites. Define a technical term before relying on it, explain why a concept exists before formalizing it, and show the intermediate reasoning that terse slides omit.
- Do not call a handout complete while a required source unit is unclassified, a lecture example is unmapped, or a high-risk OCR or answer issue remains unresolved. If source damage prevents resolution, expose it as `需人工核对` and label the delivery incomplete or partially verified.
- Make the complete review handout the main artifact. Do not replace it with only a question bank, only a memorization list, or only a last-minute summary unless the user explicitly asks.
- Prefer teacher slides, lab slides, official notices, and exam-scope files over textbooks, assignments, past exams, and senior notes.
- Use textbooks to rebuild background, definitions, proofs, and chapter logic when slides are terse.
- Use assignments and past exams to explain exam styles, common traps, and answer structure.
- Use senior notes only as supplementary references; mark unsupported claims as supplementary or needing manual verification.
- Do not create a standalone lab-content chapter by default. Add it only when the inputs include lab slides, lab manuals, lab reports, or the exam scope explicitly says lab content, lab principles, experiments, devices, measurements, or data processing will be tested.
- Do not put source catalogs, `资料说明`, `资料识别与目录梳理`, version/change notes, or a knowledge coverage table in the final handout by default. Keep those as internal working notes unless the user explicitly asks for an audit appendix.
- Do not create a standalone symbol-convention chapter by default. Explain formulas and symbols where they appear, and add only a normal formula/key-conclusion summary when useful.
- Do not compress the handout into an outline because the source set is large. Split work by chapter and produce more sections instead of omitting basic concepts, examples, figures, or source-backed explanations.
- If the user gives exam question types, build专项训练 around those types. Predictions should resemble the stated exam format rather than generic practice questions.
- Do not invent fixed answer templates. Infer answer style only from teacher-provided solutions, homework answers, sample exams, or past-exam reference answers; present it as参考答题思路 rather than a guaranteed template.
- If `名词解释`, `术语解释`, or similar term-definition questions are confirmed as an exam type, generate a separate集中背诵版 or clearly separated section. Keep entries clean for memorization: term, English name when useful, concise explanation, examples or contrast only when helpful. Do not add bracket tags such as `[原题]`, `[核心]`, or `[大写缩写]` unless the user explicitly requests labels.
- Add a short考试当天速览 or临考速记 section when useful, but let its structure fit the course instead of forcing a fixed format.
- Never fabricate unsupported conclusions. Mark uncertain OCR, missing answers, unclear images, and conflicting sources as `需人工核对`.
- Remove process text such as `根据用户要求`, `本版`, `上一版`, `自绘图`, `这里先`, `更改说明`, and draft notes before final delivery.

## Workflow

1. Inventory every input in `coverage/source-inventory.csv`; classify its source type, coverage mode, unit count, read status, and example-scan status.
2. Extract text and images from every source. OCR scanned PDFs, PPT pages, embedded slide images, exam images, and figures that may contain labels or key points. Use `extracted/` notes to preserve page, slide, figure, and source provenance.
3. Before drafting, classify each required page, slide, or source item in `coverage/source-coverage.csv`, and register every lecture example in `coverage/example-catalog.csv`.
4. Build `coverage/course-map.md` in the teacher's chapter order. Record prerequisites so later chapters do not assume unexplained concepts. For large courses, write chapter files under `sections/` and assemble them from `main.tex`.
5. Merge textbook explanations, assignments, notes, and past-exam evidence into the relevant chapters instead of creating duplicate "extra explanation" chapters.
6. Write each nontrivial knowledge point as a zero-base teaching chain: prerequisite, motivating problem, intuition, formal definition, mechanism or derivation, symbols and conditions, lecture example, mistakes, quick self-check, and exam wording. Adapt the chain to the content instead of forcing empty headings.
7. Put lecture examples beside the knowledge point they teach. Preserve the original stem and media, distinguish source-provided answers from derived solutions, and keep assignments, past exams, and predictions in clearly separated later sections.
8. Reverse-audit each drafted chapter against the coverage matrix. Keep all non-duplicate slide concepts, formulas, figures, comparisons, examples, and in-slide exercises at their original knowledge-point location.
9. Handle images deliberately: redraw simple formulas or diagrams in native LaTeX/TikZ when reliable; crop original diagrams for complex hardware, circuits, timing, waveforms, system structures, and hard-to-redraw figures.
10. Run `scripts/audit_source_coverage.py <review-project> --strict` and resolve every reported gap before declaring completion. If damaged or missing sources make that impossible, preserve the failing evidence and deliver only with an explicit incomplete/manual-check status. Then compile with XeLaTeX and inspect logs and rendered pages.
11. Final-check that the handout can replace the original course materials for a zero-base student while marking any remaining uncertain source issues.

## Resource Routing

- Read `references/workflow.md` for the full production workflow, source priority, OCR expectations, chapter writing rules, question handling, and image handling.
- Read `references/latex-style.md` before creating or editing the LaTeX project, custom boxes, tables, figures, or TikZ diagrams.
- Read `references/tooling-pitfalls.md` only when local extraction, rendering, PowerShell, PDF conversion, image generation, or file-copy commands fail or behave unexpectedly.
- Read `references/quality-checklist.md` before final delivery and again after every compile-and-render verification pass.
- Use `assets/latex-template/main.tex` as the default starting point for new review projects.
- Use `scripts/init_review_project.py` to create a review-project skeleton from the LaTeX template.
- Use `scripts/audit_source_coverage.py` to validate the source inventory, per-unit coverage, lecture-example catalog, and unresolved items before final delivery.
- Use `scripts/audit_latex_build.py` to scan `.log` files for common LaTeX build problems.

## Expected Output Shape

The default final artifact is an editable LaTeX project plus a compiled PDF. Keep `coverage/source-inventory.csv`, `coverage/source-coverage.csv`, `coverage/example-catalog.csv`, and `coverage/course-map.md` as internal evidence-bearing working artifacts; do not insert them into the PDF unless the user asks for an audit appendix. The document should normally include:

- 考试范围与复习总览
- 理论课章节知识点完整总结
- 公式与符号汇总
- 易混概念、方法与模型对比
- 作业题与概念理解整理
- 往年试卷整理
- 按用户给定题型组织的专项训练与预测题
- 名词解释集中背诵版, only when that question type is confirmed
- 考试当天速览或临考速记

Adapt section names to the actual course, but keep the separation between knowledge explanation, original questions, analysis, and formal answers. Add `实验内容整理` only when the source materials or exam scope make lab content relevant. Do not add final `资料说明`, source directories, change notes, bracket priority labels, or standalone symbol conventions unless explicitly requested.

## Quick Reference

| Need | Action |
| --- | --- |
| Scanned PDF or slide image | OCR first; do not rely on visible text only |
| Teacher slide deck or official scope | Record every page or slide in `coverage/source-coverage.csv` |
| Lecture example or in-slide exercise | Register it in `coverage/example-catalog.csv`, including answer provenance |
| Many source files | Complete source inventory and `extracted/source-name.md` notes before writing |
| Large course | Write `sections/chXX.tex` files and assemble from `main.tex` |
| Zero-base explanation | Define first use, supply prerequisites and intuition, then show steps and a worked example |
| User gives exam question types | Create专项训练 matching those exact types |
| 名词解释 is an exam type | Add a clean集中背诵版 without bracket tags |
| Teacher or past-exam answers exist | Infer参考答题思路 from them; do not invent a fixed template |
| Day-before use | Add an考试当天速览 section suited to the course |
| Complex diagram | Crop the original useful region and verify no labels/arrows are cut |
| Simple process or relation | Redraw with native LaTeX/TikZ only if correctness can be checked |
| Lecture example | Place it beside the relevant knowledge point |
| Lab slides or lab exam scope | Add a conditional lab section |
| No lab source and no lab exam scope | Do not create a lab section |
| Assignment or past exam | Preserve original stem, then add analysis and answer |
| Wide table | Split, rotate, or rewrite as list; never accept overlapping text |
| Unsupported note-only claim | Mark as supplementary or needing manual verification |
| Final handout | Run strict source coverage audit, remove process wording, and compile-check the PDF |

## Common Mistakes

- Writing a high-frequency outline instead of a complete course-replacing handout.
- Starting chapter prose before building the source-coverage and lecture-example catalogs.
- Calling coverage complete because chapter titles appear while individual slide concepts, diagrams, or exercises remain unmapped.
- Explaining a term with other undefined terms, or presenting a formula without symbols, conditions, intermediate steps, and a worked use.
- Treating OCR text as correct without checking formulas, subscripts, labels, and Chinese terms.
- Inserting whole PPT pages instead of cropping the actual useful figure.
- Mixing question stems, analysis, and answers into one paragraph.
- Duplicating a concept in "theory", "zero-base supplement", and "textbook supplement" sections instead of merging it once.
- Shrinking a large course into a short outline instead of splitting work by chapter.
- Leaving lecture examples in a detached question dump instead of explaining them near the related concept.
- Losing multi-slide example statements or solutions because only pages explicitly titled `例题` were searched.
- Adding `资料说明`, source directories, version notes, or change logs to the final handout when the user wants a polished study document.
- Adding bracket tags to memorization entries when the user needs clean背诵 material.
- Inventing universal answer templates instead of inferring answer style from teacher or past-exam solutions.
- Declaring LaTeX finished without compiling and checking the rendered PDF.
