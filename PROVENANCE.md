# Source provenance

Extracted from [mackey-bimodule-diagrams-lean](https://github.com/Alphabeta-Math/mackey-bimodule-diagrams-lean/tree/a53ee2627a1c50bb4171f743a30a288caf382083), commit `a53ee2627a1c50bb4171f743a30a288caf382083`.

All 35 registered Lean sources, their mathematical statements, and their imported supporting source files are preserved byte for byte. [The extraction manifest](evidence/extraction-manifest.json) records each module, source path, original path, imports and SHA256. The earlier accepted dependency review, translations, source attributions and compiler evidence are retained under [evidence/origin/](evidence/origin/). The original coordinator graph is reused for unchanged proof sources and the same Lean/mathlib pins; the standalone workspace receives a fresh complete build and axiom audit.

Some compatibility modules retain their original `MackeyDiagrams`, `Proofs`, and `NotesProofs` names. They are included as source in this repository; the Lake configuration requires only pinned mathlib and has no dependency on another local checkout. The original repository also retains its copy of the 35 prerequisites.

Sources: Ian X, [Abelian Categories and Bimodules](https://getcurious.cc/downloads/abelian-categories-and-bimodules-lecture-notes.pdf), with the exact theorem and page references in PROJECT.md. Mathlib and any adapted external proof fragments retain their original provenance and license information; see [EXTERNAL_PROOFS.md](EXTERNAL_PROOFS.md).
