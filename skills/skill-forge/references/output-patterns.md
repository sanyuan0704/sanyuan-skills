# Output Patterns

## Template Pattern

Provide output templates to ensure consistency across runs.

### Strict Templates (for structured output)

When exact format matters (API responses, data exports, reports):

```markdown
## Output Format

For each issue found, output:

| Field | Format |
|-------|--------|
| severity | P0 / P1 / P2 / P3 |
| location | file:line |
| description | One sentence explaining the problem |
| suggestion | One sentence with the fix |
```

### Flexible Templates (for creative output)

When structure matters but content varies:

```markdown
## Output Structure

1. **Summary** (2-3 sentences): What was done and key findings
2. **Details**: Organized by category, most important first
3. **Next Steps**: Actionable items, prioritized
```

## Example Pattern

Show input/output pairs to demonstrate expected style and detail level. Examples are more effective than verbose explanations.

### Example — Commit Messages

```markdown
## Commit Message Style

Input: Added error handling for API timeout and network errors
Output: `fix: handle API timeout and network errors gracefully`

Input: Refactored the user service to use dependency injection
Output: `refactor: use dependency injection in user service`
```

### Example — Code Review Comments

```markdown
## Comment Style

Bad: "This function is too long."
Good: "P1: `processOrder()` (142 lines) handles validation, payment, and notification.
Split into `validateOrder()`, `processPayment()`, `sendNotification()`."
```

## Pre-Delivery Checklist Pattern

Add concrete, verifiable checks before delivering output. Each item must be specific enough that the model can verify it by looking at the output.

### Organize by Category

```markdown
## Pre-Delivery Checklist

### Visual Quality
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set
- [ ] Hover states don't cause layout shift
- [ ] Brand logos are correct

### Interaction
- [ ] All clickable elements have cursor-pointer
- [ ] Transitions are smooth (150-300ms)

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] prefers-reduced-motion respected
```

### Priority-Based Output

For review/analysis skills, categorize findings by priority:

| Level | Meaning | Action |
|-------|---------|--------|
| P0 | Critical | Must block delivery / must fix immediately |
| P1 | High | Should fix before delivery |
| P2 | Medium | Create follow-up task |
| P3 | Low | Optional improvement |

This prevents the model from treating all issues as equally important. A critical security bug and a naming nitpick should not get the same weight.

### Key Rule

Every checklist item must be **specific and verifiable** — not subjective.

```markdown
# Bad
- [ ] Ensure good quality
- [ ] Make sure it looks nice

# Good
- [ ] No placeholder text remaining (TODO, FIXME, xxx)
- [ ] All generated code runs without errors
- [ ] Color contrast ratio meets WCAG AA (4.5:1 for text)
```
