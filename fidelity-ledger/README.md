# Evidence and maintenance records

The 2026-09-14 update adds five books to the existing five-source Soccer Analyst. Runtime remains `soccer-analyst/SKILL.md` and `soccer-analyst/references/`; `.agents/skills/soccer-analyst` remains a relative link to that folder. The existing repository architecture overrides the metatool's new-repository root layout. Accordingly, the actual package is validated with the tool's **nested** layout; it has not been artificially reshaped just to satisfy `--layout published-repo`.

- [Source manifest](source-manifest.json): exact supplied-file identities/hashes, editions, structural corrections and estimates. Raw sources are not included.
- [Coverage and fidelity audit](coverage-audit.md): retained methods, omissions, qualifications, corrections and source-local locators.
- [Reading ledger](reading-ledger.json) and [reading report](reading-report.json): conservative confirmed spans, repeated reads, partial/truncated views and estimated expenditure. No exhaustive coverage claim.
- [Acceptance suite](acceptance-suite.json): nine tasks frozen before semantic extraction, with development/final groups and observable criteria.
- [Evaluation status](acceptance-results.json): **unrun**; no independent baseline/core/full predictions, grades or measured improvement. [Suite validation](suite-validation.json) checks only the scenario schema.
- [Validation](validation.json): actual structural, link/preservation and scan results. An unchanged legacy football quotation triggered one reviewed MEDIUM scan finding; no HIGH findings occurred.
- [Arithmetic results](arithmetic-results.json) and [verification script](verify_examples.py): independently repeatable checks of the stated mathematical examples. No R execution or real-match model fitting.
- [Preservation baseline](preservation-baseline.json): hashes confirming the original five references and existing uncommitted `AGENTS.md` were kept intact and the latter excluded from the commit.

The master remains lean; all ten references load only when relevant. Reference sizes are deliberately below planning budgets, which are ceilings/targets rather than minimum lengths. This was a selective method expansion, not a full statistical textbook or a complete tactical coaching curriculum. The provisional density calibration from the metatool's narrative-book corpus is not treated as a validated quality score for this mixed technical corpus.

For future edits, preserve one canonical runtime copy and place provenance/evaluation records here, outside references. A future independent evaluation must save real responses and retrieval traces for baseline, core and full configurations under the same model/settings. Do not turn the present author review or arithmetic checks into passing behavioral grades.
