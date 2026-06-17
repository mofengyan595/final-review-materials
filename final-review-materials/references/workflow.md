# Workflow

Use this workflow for Chinese final-exam review handouts whose output is a detailed LaTeX project.

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

This inventory is a working artifact. Do not force it into the final PDF unless the user asks. The final PDF should not contain `资料说明`, source directories, version notes, change logs, or directory-sorting sections by default.

## Working Directories

Use the generated project directories consistently:

- `sources/`: original PDFs, PPTs, notes, assignments, exams, and scope files or symlinks/copies chosen by the user.
- `extracted/`: one Markdown extraction note per source, named like `slides-ch03.md` or `past-exam-2024.md`.
- `figures/`: cropped or redrawn figures used by LaTeX.
- `sections/`: chapter-level `.tex` files for large courses.
- `build/`: compiler output when the command supports an output directory.
- `logs/`: OCR, extraction, build, and visual-check notes.

Each `extracted/source-name.md` should record page or slide numbers, OCR text, figure indexes, crop file names, uncertain OCR, missing pages, and source-specific observations. Treat these files as the memory bridge between raw materials and the final LaTeX handout.

## OCR And Extraction

- OCR every scanned PDF page. Render pages with PyMuPDF when available; use Poppler or another reliable renderer if the local environment already provides it.
- OCR PPT pages by exporting or rendering slides to images first. Also OCR embedded slide images because key points may live inside screenshots, diagrams, labels, or formulas.
- OCR image crops with an available engine such as PaddleOCR, Tesseract, Windows OCR, or an installed project-specific OCR tool. Prefer the best available local tool; do not install new OCR dependencies without user approval.
- Save OCR output and extraction notes into `extracted/` before drafting final chapters when there is more than one source file or when OCR is nontrivial.
- For each important image, preserve page/slide provenance and a short description.
- Check formulas, subscripts, superscripts, Greek letters, Chinese technical terms, arrows, axes, and circuit/interface labels manually after OCR.
- Mark uncertain OCR as `需人工核对`; do not silently normalize unclear terms.

## Chapter Planning And Section Files

For small courses, writing directly in `main.tex` is acceptable. For large courses or many source files:

1. Build a chapter map from teacher materials first.
2. Map textbook, assignment, past-exam, and note content into that chapter map.
3. Create one file per chapter under `sections/`, such as `sections/ch01-intro.tex`.
4. Assemble section files from `main.tex` using `\input{sections/ch01-intro}`.
5. Keep chapter-local figures near their chapter in naming, such as `figures/ch03-cache-mapping.png`.

If content is too large for one pass, split generation into chapters. Do not shorten explanations, drop examples, or omit basic concepts to fit a single response.

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

Do not include `资料说明`, `资料识别与目录梳理`, source catalogs, version/change notes, or standalone symbol-convention pages in the final handout by default. Explain symbols beside formulas and use a formula/key-conclusion summary when useful. Add a short考试当天速览 or临考速记 section near the end when it helps last-minute review; choose its shape freely based on the course and exam types.
