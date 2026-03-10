---
name: code-review-expert
description: "Expert code review of current git changes with a senior engineer lens. Detects SOLID violations, security risks, and proposes actionable improvements."
---

# Code Review Expert

## Overview

Perform a structured review of the current git changes with focus on SOLID, architecture, removal candidates, and security risks. Default to review-only output unless the user asks to implement changes.

## Severity Levels

| Level | Name | Description | Action |
|-------|------|-------------|--------|
| **P0** | Critical | Security vulnerability, data loss risk, correctness bug | Must block merge |
| **P1** | High | Logic error, significant SOLID violation, performance regression | Should fix before merge |
| **P2** | Medium | Code smell, maintainability concern, minor SOLID violation | Fix in this PR or create follow-up |
| **P3** | Low | Style, naming, minor suggestion | Optional improvement |

## Workflow

### 1) Preflight context

- Load `references/project-brain.md` to identify project-specific constraints that override or refine generic best practices.
- Use `git status -sb`, `git diff --stat`, and `git diff` to scope changes.
- **Language Detection**: Identify the primary languages in the diff. Explicitly recall and apply common "footguns" and idioms for those languages (e.g., Python's mutable defaults, JS event loop blocking, Go's goroutine leaks).
- **Impact Analysis (Low-Token Strategy)**:
  - If an exported function, method, or type signature has changed:
    1. Run `rg "nameOfIdentifier" --stats` to see how many times it's used.
    2. If the count is low (<10), run `rg -C 2 "nameOfIdentifier"` to view the call sites directly in the terminal output.
    3. If the count is high, only check the most critical files based on the project structure (e.g., those in `routes/`, `controllers/`, or `main`).
  - **Do not read the whole file** unless the logic at the call site is too complex to understand from the 2-line context.
- Identify entry points, ownership boundaries, and critical paths (auth, payments, data writes, network).
- **Dependency Discovery (Ripple Effect)**:
  - Enumerate any changed public contracts: exported functions, return types, DTOs, events, env var names, feature flags, and database schema/migrations.
  - For each contract, map downstream consumers with `rg -n "ContractName"` (or related key strings) across the repo; skim unchanged files to confirm expectations still hold.
  - Check caller assumptions: error shapes, nullability, timing/async behavior, and side effects (e.g., logging, metrics, transactions).
  - Note high-risk boundaries (auth, payments, persistence, external APIs) where contract drift is most likely to break runtime behavior.

**Edge cases:**
- **No changes**: If `git diff` is empty, inform user and ask if they want to review staged changes or a specific commit range.
- **Large diff (>500 lines)**: Summarize by file first, then review in batches by module/feature area.
- **Mixed concerns**: Group findings by logical feature, not just file order.

### 2) SOLID + architecture smells

- Load `references/solid-checklist.md` for specific prompts.
- Look for:
  - **SRP**: Overloaded modules with unrelated responsibilities.
  - **OCP**: Frequent edits to add behavior instead of extension points.
  - **LSP**: Subclasses that break expectations or require type checks.
  - **ISP**: Wide interfaces with unused methods.
  - **DIP**: High-level logic tied to low-level implementations.
- When you propose a refactor, explain *why* it improves cohesion/coupling and outline a minimal, safe split.
- If refactor is non-trivial, propose an incremental plan instead of a large rewrite.

### 3) Removal candidates + iteration plan

- Load `references/removal-plan.md` for template.
- Identify code that is unused, redundant, or feature-flagged off.
- Distinguish **safe delete now** vs **defer with plan**.
- Provide a follow-up plan with concrete steps and checkpoints (tests/metrics).

### 4) Security and reliability scan

- Load `references/security-checklist.md` for coverage.
- Check for:
  - XSS, injection (SQL/NoSQL/command), SSRF, path traversal
  - AuthZ/AuthN gaps, missing tenancy checks
  - Secret leakage or API keys in logs/env/files
  - Rate limits, unbounded loops, CPU/memory hotspots
  - Unsafe deserialization, weak crypto, insecure defaults
  - **Race conditions**: concurrent access, check-then-act, TOCTOU, missing locks
- Call out both **exploitability** and **impact**.

### 5) Code quality scan

- Load `references/code-quality-checklist.md` for coverage.
- **Dynamic Language Heuristics**: Identify the language paradigm and apply specific "expert" checks:
  - **Memory Management**: Check for manual management risks (C/C++/Zig/Rust) vs. GC pressures/leaks (Java/JS/Python).
  - **Type Safety**: Flag "type-cheating" (TypeScript `any`, Python `Any`, Go `interface{}`) or unsafe type casting.
  - **Concurrency Models**: Look for race conditions specific to the model (Threads/Locks, Goroutines/Channels, or JS Event Loop).
  - **Infrastructure/DSL**: If reviewing SQL, YAML, or Terraform, focus on injection, schema-locking, or resource-leakage.
- Check for:
  - **Error handling**: swallowed exceptions, overly broad catch, missing error handling, async errors.
  - **Performance**: N+1 queries, CPU-intensive ops in hot paths, missing cache, unbounded memory.
  - **Boundary conditions**: null/undefined handling, empty collections, numeric boundaries, off-by-one.

### 6) Output format

Structure your review as follows:

```markdown
## Code Review Summary

**Files reviewed**: X files, Y lines changed
**Overall assessment**: [APPROVE / REQUEST_CHANGES / COMMENT]

---

## Findings

### P0 - Critical
(none or list)

### P1 - High
1. **[file:line]** Brief title
  - Description of issue
  - Suggested fix

### P2 - Medium
2. (continue numbering across sections)
  - ...

### P3 - Low
...

---

## Removal/Iteration Plan
(if applicable)

## Additional Suggestions
(optional improvements, not blocking)
```

**Inline comments**: Use this format for file-specific findings:
```
::code-comment{file="path/to/file.ts" line="42" severity="P1"}
Description of the issue and suggested fix.
::
```

**Clean review**: If no issues found, explicitly state:
- What was checked
- Any areas not covered (e.g., "Did not verify database migrations")
- Residual risks or recommended follow-up tests

### 7) Next steps confirmation

After presenting findings, ask user how to proceed:

```markdown
---

## Next Steps

I found X issues (P0: _, P1: _, P2: _, P3: _).

**How would you like to proceed.**

1. **Fix all** - I'll implement all suggested fixes
2. **Fix P0/P1 only** - Address critical and high priority issues
3. **Fix specific items** - Tell me which issues to fix
4. **No changes** - Review complete, no implementation needed

Please choose an option or provide specific instructions.
```

**Important**: Do NOT implement any changes until user explicitly confirms. This is a review-first workflow.

## Resources

### references/

| File | Purpose |
|------|---------|
| `solid-checklist.md` | SOLID smell prompts and refactor heuristics |
| `security-checklist.md` | Web/app security and runtime risk checklist |
| `code-quality-checklist.md` | Error handling, performance, boundary conditions |
| `removal-plan.md` | Template for deletion candidates and follow-up plan |
