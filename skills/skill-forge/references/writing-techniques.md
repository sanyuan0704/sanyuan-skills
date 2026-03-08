# Writing Techniques for Skills

## Technique 1: The Iron Law

Set one unbreakable rule at the top of SKILL.md, right after frontmatter. This prevents the model from taking shortcuts.

### Examples

**Debugging skill:**
```
IRON LAW: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
```

**TDD skill:**
```
IRON LAW: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
```

**Copywriting skill:**
```
IRON LAW: Clarity over cleverness — ALWAYS.
```

**Database migration skill:**
```
IRON LAW: Every migration must have a rollback script. No rollback = no execution.
```

### How to Write an Iron Law

Ask: "What is the ONE mistake the model will most likely make with this skill?"

Then write a rule that prevents it:
- ALL CAPS for emphasis
- Absolute language ("NEVER", "ALWAYS", "MUST")
- No wiggle room — no "try to" or "consider"

### Red Flag Signals

Pair your Iron Law with "red flags" that force the model to backtrack when it drifts:

```markdown
Red Flags (return to Step 1 if any appear):
- "I think the problem might be..." (guessing, not analyzing)
- Making changes without understanding root cause
- Fix works but you can't explain why
```

This is a "rollback mechanism" — when the model catches itself drifting, it resets to the investigation phase.

## Technique 2: Question-Style Instructions

Give the model specific questions to answer, not vague directives. Models excel at "finding answers to specific questions" but struggle with abstract instructions.

### Why This Works

A good question focuses the model's attention on the right part of the code or content. A vague directive leaves the model unsure where to look.

### Examples

```markdown
# Bad — vague directive
Check if the code violates the Single Responsibility Principle.

# Good — specific question
Ask yourself: How many distinct reasons could this module need to change?
If the answer is more than one, it likely violates SRP.
```

```markdown
# Bad
Watch out for race conditions.

# Good
Ask: What happens if two requests hit this code simultaneously?
```

```markdown
# Bad
Handle edge cases properly.

# Good
Ask: What happens if this value is null? Is 0? Is an empty array? Is negative?
```

```markdown
# Bad
Watch out for TOCTOU vulnerabilities.

# Good
Ask: Between checking the permission and performing the action,
could the state have changed?
```

```markdown
# Bad
Write engaging copy.

# Good
Ask: If the reader stopped after the first sentence, would they know
what they're getting and why they should care?
```

### Pattern

Transform vague directives into concrete questions:

1. Identify what you want the model to check
2. Ask the question a senior expert would ask when checking it
3. Include what the answer implies ("if more than one → likely violates SRP")

## Technique 3: Anti-Pattern Documentation

Explicitly list what the model should NOT do. This is as important as listing what it should do.

### Why This Works

Models have "default patterns" from training data — purple/blue gradients for UI, "Learn More" for CTAs, try-catch-console.log for error handling. If you only say "write good UI," the model uses its defaults. But if you say "NOT purple gradients, NOT Inter font, NOT rounded card grids," it's forced out of its comfort zone.

### How to Find Anti-Patterns

Ask: "What would Claude's lazy default look like for this task?" Then explicitly forbid it.

### Examples

**Frontend design skill:**
```markdown
Anti-Patterns to Avoid:
- Generic AI aesthetics
- Purple/blue gradients as default
- Cookie-cutter layouts
- Overused fonts like Inter for everything
- Avoid designs that look "AI-generated"
```

**Copywriting skill:**
```markdown
Weak CTAs to avoid: "Submit", "Sign Up", "Learn More"
```

**Code review skill:**
```markdown
Insecure patterns (must flag):
- Direct SQL string concatenation
- User input inserted into HTML without escaping
- Check-then-act without locks
- Hardcoded secrets or credentials
```

**Any skill that generates code:**
```markdown
Do NOT:
- Add unnecessary try-catch blocks with console.log
- Over-abstract one-time operations into utility functions
- Add comments that restate the code
- Create configuration for things that won't change
```

### Structure

Place anti-patterns either:
- In the SKILL.md body near the relevant step
- In a reference file for detailed anti-pattern lists (e.g., `references/security-antipatterns.md`)

Keep them concrete and specific — not "don't write bad code" but "don't concatenate SQL strings."
