# Tooling Pitfalls

Use this only for local toolchain problems while extracting, rendering, compiling, copying, or verifying Chinese LaTeX review handouts. Do not treat these notes as document-structure rules.

## Windows And Paths

- Use `-LiteralPath` only for literal paths. It does not expand wildcards; enumerate files with `Get-ChildItem` before copying or processing multiple files.
- Paths with Chinese characters, spaces, or parentheses should be quoted and verified with `Test-Path`, `Resolve-Path`, or `Get-Item` before assuming a tool failed for content reasons.
- Terminal output may show Chinese paths as mojibake even when files are correct. Verify by reading the file, resolving the path, or inspecting the generated PDF/image.

## PDF And Image Rendering

- Some PDF rendering wrappers fail on Chinese paths. If a Poppler-based command fails with path or encoding symptoms, try rendering through PyMuPDF from the Codex tools Python environment.
- Image files may fail to overwrite when open in a viewer. Render into a fresh output directory or versioned filename instead of repeatedly overwriting the same image.
- Treat `pdftotext` as a search and sanity tool only. It cannot prove that formulas, boxes, TikZ figures, cropped images, or page breaks render correctly.

## Verification

- Compile with XeLaTeX enough times for the table of contents and references to settle.
- Scan logs for fatal errors, undefined control sequences, missing files, missing characters, overfull boxes, undefined references, and rerun warnings.
- Render and inspect representative pages from risky areas: dense formulas, TikZ diagrams, cropped figures, long question boxes, homework answers, and new practice sections.
