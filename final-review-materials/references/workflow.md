# Workflow

Use this workflow for Chinese final-exam review handouts whose output is a detailed LaTeX project.

## Contents

- Source Priority
- Input Inventory
- Working Directories
- Evidence Gates Before Drafting
- OCR And Extraction
- Chapter Planning And Section Files
- Zero-Base Teaching Contract
- Chapter Reconstruction
- Conditional Lab Content
- Lecture Example Discovery And Cataloging
- Questions
- Image Handling
- Final Document

## Source Priority

1. Teacher theory slides, lab slides, official exam scope, notices, and in-class emphasis.
2. Textbook PDFs for definitions, background, derivations, and complete chapter logic.
3. Past exams, sample exams, mock exams, and final-related papers for question style and common test points.
4. Assignments and answer keys for reasoning, common mistakes, and concept reinforcement.
5. Senior notes as supplementary checks only.

When sources conflict, use teacher and official materials first. Add a short note near the affected content: `资料之间存在差异，已优先采用教师课件/实验课件/教师资料。`

## Input Inventory

Before drafting the handout, list each source file with:

- File name and path.
- Source type.
- Covered chapters or topics.
- Main knowledge points.
- Lab topics and equipment/processes, if any.
- Assignment or exam question list.
- OCR risks, missing pages, unclear images, incomplete answers, or unreadable formulas.

Also record each source in `coverage/source-inventory.csv`:

- `source_file`: stable path or file name used by the other coverage files.
- `source_type`: theory slides, lab slides, official scope, textbook, assignment, answer key, past exam, senior note, or other.
- `coverage_mode`: `page` for slides and page-addressable official material, `item` for question sets or other countable units, and `reference` for sources used selectively to deepen explanations.
- `unit_count`: total pages, slides, or countable items when the mode is `page` or `item`.
- `read_status`: `pending`, `complete`, `partial`, or `unreadable`.
- `example_scan_status`: `pending`, `complete`, `partial`, or `not-applicable`.
- `notes`: scope limits, missing pages, OCR risks, or reasons for `not-applicable`.

Use `page` coverage for every teacher theory deck, lab deck, and official exam-scope file. Use `reference` for a large textbook only when the user did not ask for full textbook coverage and only selected chapters are relevant.
For `page` coverage, normalize `unit_id` to consecutive integers `1` through `unit_count` in visual page or slide order. Record printed page numbers separately in extraction notes when they differ.

This inventory is a working artifact. Do not force it into the final PDF unless the user asks. The final PDF should not contain `资料说明`, source directories, version notes, change logs, or directory-sorting sections by default.

## Working Directories

Use the generated project directories consistently:

- `sources/`: original PDFs, PPTs, notes, assignments, exams, and scope files or symlinks/copies chosen by the user.
- `extracted/`: one Markdown extraction note per source, named like `slides-ch03.md` or `past-exam-2024.md`.
- `coverage/`: source inventory, per-unit coverage, lecture-example catalog, and course map used as internal evidence.
- `figures/`: cropped or redrawn figures used by LaTeX.
- `sections/`: chapter-level `.tex` files for large courses.
- `build/`: compiler output when the command supports an output directory.
- `logs/`: OCR, extraction, build, and visual-check notes.

Each `extracted/source-name.md` should record page or slide numbers, OCR text, figure indexes, crop file names, uncertain OCR, missing pages, and source-specific observations. Treat these files as the memory bridge between raw materials and the final LaTeX handout.

## Evidence Gates Before Drafting

Do not start chapter prose after only skimming file names or extracting a single text dump. First establish these internal working artifacts:

1. `coverage/source-inventory.csv`: one row per input source.
2. `coverage/source-coverage.csv`: one row per required page, slide, or item.
3. `coverage/example-catalog.csv`: one row per lecture example, worked demonstration, in-slide exercise, or question-like prompt.
4. `coverage/course-map.md`: teacher-order chapter map, knowledge-point IDs, prerequisites, source anchors, and planned output files.

For `source-coverage.csv`, use these normalized statuses:

- `mapped`: substantive content is written into the stated output location.
- `merged`: true duplicate content is merged into another mapped knowledge point; keep the destination in `output_location`.
- `non-content`: title, divider, navigation, decoration, or genuinely empty material; explain briefly in `uncertainty` or `extracted_items`.
- `needs-review`: OCR, source damage, answer conflict, or interpretation remains unresolved.

Each row should preserve the source unit, unit type, knowledge-point ID, extracted concepts/formulas/figures/examples, output location, status, and uncertainty. Do not leave a page absent because it looks unimportant; record it and classify it.

Before final delivery, run:

```text
python scripts/audit_source_coverage.py <review-project> --strict
```

Use the project interpreter or the approved one-off document tool environment. Strict mode must fail while units are missing, example scanning is incomplete, mapped content lacks an output location, or any unresolved warning remains.

## OCR And Extraction

- OCR every scanned PDF page. Render pages with PyMuPDF when available; use Poppler or another reliable renderer if the local environment already provides it.
- OCR PPT pages by exporting or rendering slides to images first. Also OCR embedded slide images because key points may live inside screenshots, diagrams, labels, or formulas.
- OCR image crops with an available engine such as PaddleOCR, Tesseract, Windows OCR, or an installed project-specific OCR tool. Prefer the best available local tool; do not install new OCR dependencies without user approval.
- Save OCR output and extraction notes into `extracted/` before drafting final chapters when there is more than one source file or when OCR is nontrivial.
- For each important image, preserve page/slide provenance and a short description.
- Inspect pages visually for examples even when OCR finds no `例题` keyword. Question-like material may appear as screenshots, diagrams, code, worked calculations, `Example`, `课堂练习`, `思考`, `试一试`, `习题`, prompts ending in a question mark, or a setup whose solution appears on later slides.
- Check formulas, subscripts, superscripts, Greek letters, Chinese technical terms, arrows, axes, and circuit/interface labels manually after OCR.
- Mark uncertain OCR as `需人工核对`; do not silently normalize unclear terms.

## Chapter Planning And Section Files

For small courses, writing directly in `main.tex` is acceptable. For large courses or many source files:

1. Build a chapter map from teacher materials first.
2. Assign stable knowledge-point IDs and record prerequisite relationships in `coverage/course-map.md`.
3. Map textbook, assignment, past-exam, and note content into that chapter map.
4. Create one file per chapter under `sections/`, such as `sections/ch01-intro.tex`.
5. Assemble section files from `main.tex` using `\input{sections/ch01-intro}`.
6. Keep chapter-local figures near their chapter in naming, such as `figures/ch03-cache-mapping.png`.

If content is too large for one pass, split generation into chapters. Do not shorten explanations, drop examples, or omit basic concepts to fit a single response.

## Zero-Base Teaching Contract

Write for a student who has not attended the lectures and may not know the chapter's assumed vocabulary. For each nontrivial concept, method, formula, protocol, system, or experiment, build a teaching chain with the applicable elements below:

1. Prerequisites: name and briefly recover the earlier ideas needed here.
2. Motivating problem: explain what difficulty the concept solves and why the older approach is insufficient.
3. Intuition: give a plain-language mental model before formal terminology.
4. Formal definition: introduce the precise term only after the reader has a foothold.
5. Mechanism or derivation: show intermediate states, causal steps, or mathematical transitions instead of jumping to the result.
6. Symbols and conditions: explain every symbol, unit, direction, assumption, valid range, and applicability condition at first use.
7. Lecture example: work through the source example step by step and connect each step to the rule just taught.
8. Mistake or counterexample: show the most likely wrong interpretation and why it fails.
9. Quick self-check: add a short recall, judgment, or one-step application when it materially helps learning.
10. Exam wording: show how the same idea can appear in the confirmed or source-inferred exam format.

Adapt this chain to the content. Do not create empty repetitive headings for a trivial definition, but do not omit prerequisites, intermediate reasoning, or a worked use merely because the slides are terse.

Apply these hard readability rules:

- Define a technical term before using it to explain another new term.
- Expand abbreviations at first use unless the course treats them as universally known.
- Explain what to observe in a figure, table, waveform, or code fragment; a caption alone is not teaching.
- For formulas used in calculations, include at least one source example or a clearly labeled derived micro-example when the source has none.
- Distinguish a memory aid from the full explanation; mnemonics and summary tables cannot replace teaching prose.

## Chapter Reconstruction

Use the teacher's course order as the backbone. For every chapter or topic, write complete explanations that include:

- Chapter knowledge frame.
- Core and basic concepts.
- Definitions, background, and intuition.
- Important formulas, symbol meanings, and applicable conditions.
- Derivations or algorithm steps when relevant.
- Methods, models, system structures, or experimental principles.
- Lecture examples and important figures.
- Textbook supplements.
- Assignment connections.
- Past-exam appearances and likely question wording.
- Mistakes, traps, and chapter summary.

For algorithms, models, and methods, include: basic idea, inputs, outputs, steps, formulas, applicable scenarios, advantages, limitations, example, and comparison with similar methods.

Do not create separate chapters named `零基础补充`, `全量扩充`, or `课本补充`. Fold those explanations into the right theory chapter or into the conditional lab chapter when the lab gate is met.

Write in a textbook-like review style: long-form explanations first, then exam hints in context, then a chapter summary. Do not replace teaching paragraphs with terse lists unless the content is naturally a checklist or comparison.

Place lecture examples directly under the concept, formula, algorithm, or experiment they teach. Do not move lecture examples into a detached question bank unless the user explicitly asks.

After drafting a chapter, reverse-audit every `mapped` or `merged` coverage row assigned to that chapter. Confirm that the final prose still contains every non-duplicate concept, mechanism, field meaning, formula, comparison, figure, example, and in-slide exercise. Add missing substance at the original knowledge-point location; do not create a detached `补充知识点` block.

Keep the complete review handout as the main artifact. Exam-type practice, memorization packs, and last-minute summaries should supplement the full chapter explanation, not replace it.

## Conditional Lab Content

Do not create a standalone lab chapter by default. Create `实验内容整理` only when at least one of these is true:

- The input set includes lab slides, lab manuals, lab reports, experiment handouts, or device/procedure worksheets.
- The teacher's exam scope explicitly says lab content, lab principles, experiments, devices, measurements, data processing, waveforms, wiring, or experimental phenomena will be tested.
- Past exams clearly include lab-analysis questions and the current course materials include enough lab source material to support explanations.

If none of these conditions is met, omit the lab chapter entirely and do not invent generic lab content.

When the lab gate is met, each lab topic should include:

- Lab name, purpose, background, and principle.
- Key concepts and formulas.
- Equipment, system composition, hardware/software structure, or circuit/connectivity.
- Procedure and data-processing method.
- Common phenomena, error sources, and precautions.
- Possible exam questions.
- Relationship to theory chapters.

Do not write lab sections as experiment reports. Explain what the lab proves, why steps are used, and how it can be examined.

## Lecture Example Discovery And Cataloging

Treat lecture examples as source content, not optional practice. Search both extracted text and rendered pages for:

- explicit labels such as `例`, `例题`, `Example`, `课堂练习`, `思考`, `试一试`, and `习题`;
- question marks, given conditions, requested outputs, fill-in blanks, calculations, code traces, diagrams to analyze, and teacher demonstrations;
- a problem introduced on one slide and solved incrementally across later slides;
- screenshots or embedded images containing a stem, options, table, graph, waveform, circuit, or answer.

Register each example in `coverage/example-catalog.csv` before writing it. Preserve:

- a stable `example_id`, source file, and page/slide/item identifier;
- example type and mapped knowledge-point ID;
- whether the full stem is complete;
- whether necessary media is preserved, faithfully redrawn, unnecessary, or still needs review;
- answer provenance: teacher/source answer, derived solution, missing answer, or unresolved conflict;
- final output location, mapping status, and uncertainty.

Use `mapped`, `merged`, or `needs-review` for example status. `merged` is allowed only for a genuinely duplicate example and must point to the retained output location.
Use `complete`, `partial`, or `unreadable` for stem status; `not-needed`, `preserved`, `redrawn`, or `needs-review` for media status; and `teacher`, `source`, `derived`, `missing`, `conflict`, or `needs-review` for answer source.

In the final chapter:

- Preserve the original stem and subparts in source order.
- State what the example teaches before solving it when that helps a beginner.
- For calculations, expose known quantities, target, rule selection, substitution, intermediate steps, units, result, and sanity check.
- For conceptual, code, diagram, or design examples, use an equivalent explicit reasoning sequence suited to the task.
- Label a reconstructed answer as `推导解答` or `参考解答`; never present it as the teacher's answer.
- Keep a multi-slide solution together even when its stem and answer were extracted from different pages.
- Keep the full worked example beside its knowledge point. A compact example index may point to it, but must not duplicate or replace it.

## Questions

Keep question sources separated:

- Lecture examples: place near the relevant knowledge point in theory chapters, or in the conditional lab chapter when the example is truly lab-specific.
- Assignments: collect in the assignment section after their concepts have already been explained in the main chapters.
- Past exams: collect in the past-exam section, preserving paper/year order when possible.
- Prediction questions: keep separate from real questions and state the evidence basis.

When the user provides exam question types, create专项训练 sections that match those types exactly, such as 名词解释、简答、计算/应用、选择、判断、程序/代码分析、设计题, or any course-specific format. If no question types are provided, infer likely types from past exams and sample exams, but mark the inference as uncertain.

Do not invent fixed answer templates. If teacher solutions, homework answers, sample answers, or past-exam reference answers are available, summarize their answer style as参考答题思路, for example common depth, step order, calculation presentation, or wording habits. If such sources are missing, give only general answering advice.

If 名词解释 or 术语解释 is confirmed as an exam type, generate a clean集中背诵版 or separated section. Use concise entries designed for memorization:

- Term in Chinese, with English name or abbreviation only when useful.
- Definition and role.
- Key mechanism, condition, or contrast when it helps distinguish similar terms.
- One short example only when it improves recall.

Do not add bracket tags such as `[原题]`, `[核心]`, `[高频]`, or `[大写缩写]` to memorization entries unless the user explicitly asks for tags. Avoid source labels and priority labels that interrupt recitation.

For assignments and past exams:

- Preserve the original question stem and original order when possible.
- Keep question, knowledge point, analysis, formal answer, and mistakes visually separate.
- Expand analysis enough for a weak student to understand the reasoning.
- Highlight the formal answer.
- Keep options on separate lines for multiple-choice questions.
- Preserve question images and answer images; crop or redraw only when reliable.
- Mark unsupported or unofficial answers as `参考答案需人工核对`.

Prediction questions should follow the stated or inferred exam question types. Prefer same-type variants of teacher examples, assignments, sample exams, and past exams over generic invented questions.

## Image Handling

- Do not insert whole PPT pages unless the whole page is one complete necessary figure.
- Crop only the useful figure, table, waveform, timing chart, hardware structure, process, interface, coordinate system, or circuit.
- Check that labels, arrows, axes, waveforms, legends, pin names, and key text are not cut off.
- After inserting a crop into LaTeX, render the target PDF page and inspect the rendered page. Checking the source crop alone is not enough.
- Confirm that axes, arrows, interface names, pin labels, legends, formula labels, waveform edges, and nearby explanatory text remain visible at the final scale.
- Prefer original crops for complex hardware diagrams, system diagrams, circuits, waveforms, timing diagrams, and diagrams with many labels.
- Use native LaTeX/TikZ for formulas, simple tables, simple process diagrams, or clean concept diagrams when correctness can be checked.
- Every figure needs a caption and explanatory text near the related knowledge point.

## Final Document

The final document should read as a polished review handout, not a work log. It should be detailed, non-duplicative, source-faithful, and directly compilable.

Completeness is a hard requirement. If time, context, or document size becomes limiting, stop at a clean chapter boundary and continue in the next chapter; do not silently reduce depth.

Do not claim completion until the strict source-coverage audit passes. If missing or damaged source material makes a clean audit impossible, preserve the failing result, label the delivery incomplete or partially verified, and surface every warning as a manual-check item. Page count, word count, chapter-title presence, or a clean LaTeX log is not evidence of source completeness.

Do not include `资料说明`, `资料识别与目录梳理`, source catalogs, version/change notes, or standalone symbol-convention pages in the final handout by default. Explain symbols beside formulas and use a formula/key-conclusion summary when useful. Add a short考试当天速览 or临考速记 section near the end when it helps last-minute review; choose its shape freely based on the course and exam types.
