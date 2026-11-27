# Build and audit

```sh
lake update
lake exe cache get
lake build
lake env lean evidence/exported-correspondence-axioms.lean
```

`lake build` builds the complete `EilenbergWatts` library, including all 35 results and the original-form adapter. No sibling repository or absolute source path is required. Lean and mathlib revisions are pinned in lean-toolchain and lakefile.toml.

On a memory-limited host, `python3 scripts/build.py` builds the local import closure in dependency order before the aggregate library. The proof and external-dependency graphs are available in DEPENDENCIES.md and proof-graph.json; README.md shows 20 landmarks.
