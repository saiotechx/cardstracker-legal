# ECC v3.1 — Verification governance

**This document provides behavioral rules and an initial CI preflight, not a universal guarantee of correctness.** Read AGENTS.md before work.

- Before: identify the exact requested deliverable, primary source, acceptance criteria, permissions, protected baseline, and feasible verification.
- Implement: perform that deliverable; preserve existing behavior; do not substitute plans, unrelated findings, or fabricated evidence.
- Verify: associate every material claim with an actual test, source observation, or external readback. CI exit codes alone do not prove features work.
- Never claim *analyzed*, *tested*, *built*, *deployed*, *fixed*, *saved* or *complete* if the underlying operation or check was not performed.
- Report status COMPLETE/PARTIAL/BLOCKED/FAILED with PERFORMED, VERIFIED, EVIDENCE, UNVERIFIED, REGRESSIONS CHECKED, REMAINING BLOCKERS.
- Never modify verification criteria or tests just to secure a PASS. Require human review and controlled branch rules for release-critical updates.
- This baseline CI preflight is not task-specific acceptance evidence. Every task still requires its own relevant proof and regression coverage.
- All workflow modifications remain on a review branch until explicitly merged. Do not assume merge protection is active.
