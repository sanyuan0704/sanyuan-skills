# Workflow Patterns

## The Checklist Pattern

A trackable checklist gives the model a clear execution path. Without one, the model freestyles — inconsistent, skipping steps, mixing priorities.

### Basic Structure

```markdown
Copy this checklist and check off items as you complete them:

- [ ] Step 1: Setup & Analyze
  - [ ] 1.1 Load preferences
  - [ ] 1.2 Analyze content
  - [ ] 1.3 Check existing ⚠️ REQUIRED
- [ ] Step 2: Confirmation ⚠️ REQUIRED
- [ ] Step 3: Execute core task
- [ ] Step 4: Review & output
```

### Markers

| Marker | Meaning | When to Use |
|--------|---------|-------------|
| ⚠️ REQUIRED | Must not skip | User confirmation, critical validation |
| ⛔ BLOCKING | Must complete before proceeding | Prerequisite setup, dependency loading |
| (conditional) | Execute based on earlier decisions | Optional review, user-selected features |

### Design Principles

1. **Progressive depth**: Start macro, go micro. Don't start with naming conventions — start with understanding the overall change.
2. **Sub-step nesting**: Complex steps broken into 1.1, 1.2, 1.3.
3. **Conditional branches**: Mark steps that only run in certain scenarios.

### Example — PPT Generation Workflow

```markdown
- [ ] Step 0: Check preferences ⛔ BLOCKING
  - [ ] Found → load preferences → continue
  - [ ] Not found → run first-time setup → MUST complete before Step 1
- [ ] Step 1: Analyze content
- [ ] Step 2: Confirm options ⚠️ REQUIRED
- [ ] Step 3: Generate outline
- [ ] Step 4: Review outline (conditional — only if user opted in)
- [ ] Step 5: Generate slides
- [ ] Step 6: Output summary
```

### Example — Code Review Workflow (Progressive Depth)

```markdown
- [ ] Step 1: Understand scope (what changed and why)
- [ ] Step 2: Architecture review (does the design make sense?)
- [ ] Step 3: Security review → Load security-checklist.md
- [ ] Step 4: Code quality → Load quality-checklist.md
- [ ] Step 5: Present findings ⚠️ REQUIRED
- [ ] Step 6: Apply fixes (only after user confirms which ones)
```

Note: The order matters. Good reviewers don't start with naming conventions — they start with understanding intent. The workflow reflects this.

## Confirmation Gates

Force the model to stop and ask the user before critical operations.

### When to Add Confirmation Gates

- Before any destructive operation (delete, overwrite, modify)
- Before any generative operation with significant compute cost
- Before applying changes based on analysis
- When user preferences affect the output

### Pattern 1: Simple Gate

```markdown
## Step 5: Confirm ⚠️ REQUIRED

Present findings to the user. Ask:
- Proceed with all recommendations?
- Only apply high-priority (P0/P1) items?
- Select specific items to apply?
- View only, no changes?

⚠️ Do NOT proceed without explicit user confirmation.
```

### Pattern 2: Structured Gate (using AskUserQuestion)

```markdown
## Step 2: Confirm Options ⚠️ REQUIRED

Use AskUserQuestion to confirm:
- Round 1 (always): style, audience, quantity, review preferences
- Round 2 (conditional): only if "custom" was selected — texture, tone, layout

Unless user passed `--quick` flag, this step is mandatory.
```

### Pattern 3: Blocking Gate

```markdown
## Step 0: Load Preferences ⛔ BLOCKING

- Found → load and continue
- Not found → run first-time setup → MUST complete before Step 1
```

### Why Confirmation Gates Matter

Without them, if the model makes a wrong decision at step 3, everything after step 3 is wasted work. Gates give users control over the process and ensure the model's analysis is reviewed before action.

## Pre-Delivery Checklist Pattern

Add concrete, verifiable checks before delivering output. Each item must be specific enough to check by looking at the output.

### Bad vs Good

```markdown
# Bad — vague, uncheckable
- [ ] Ensure good quality
- [ ] Make sure it's accessible

# Good — specific, verifiable
- [ ] No emojis used as icons (use SVG instead)
- [ ] All images have alt text
- [ ] All clickable elements have cursor-pointer
- [ ] Transitions are 150-300ms
- [ ] No placeholder text remaining (TODO, FIXME, xxx)
```

### Organize by Category

```markdown
## Pre-Delivery Checklist

### Correctness
- [ ] Generated code compiles/runs without errors
- [ ] Output matches requested format exactly
- [ ] No placeholder text remaining

### Quality
- [ ] Follows existing code style in the project
- [ ] No unnecessary complexity added

### Completeness
- [ ] All workflow checklist items checked off
- [ ] User's original request fully addressed
```

### Priority-Based Output

For review/analysis skills, categorize findings instead of a flat list:

| Level | Meaning | Action |
|-------|---------|--------|
| P0 | Critical | Must block delivery |
| P1 | High | Should fix before delivery |
| P2 | Medium | Create follow-up task |
| P3 | Low | Optional improvement |

This prevents the model from treating all issues equally — critical bugs and naming nitpicks should not get the same weight.
