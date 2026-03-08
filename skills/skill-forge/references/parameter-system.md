# Parameter System

## The $ARGUMENTS Variable

Skills receive user input through the `$ARGUMENTS` variable. This includes everything the user types after the skill invocation.

Example: `/my-skill article.md --style dark --quick`
→ `$ARGUMENTS` = `article.md --style dark --quick`

## Designing Parameters

### Basic Structure

Document parameters as a table in SKILL.md:

```markdown
## Options

| Option | Description | Default |
|--------|-------------|---------|
| `<content>` | Input file or text | Required |
| `--style <name>` | Visual style | auto |
| `--quick` | Skip confirmation gates | false |
| `--lang <code>` | Output language | en |
```

### Parameter Types

1. **Positional**: `<content>` — the main input
2. **Named flags**: `--style dark` — configuration with a value
3. **Boolean flags**: `--quick` — toggle behavior (no value)
4. **Partial execution**: `--outline-only`, `--images-only` — run only part of the workflow
5. **Selective redo**: `--regenerate 3` — redo a specific item without rerunning everything

### Argument Hint

Add `argument-hint` to frontmatter so users see parameter suggestions when typing `/`:

```yaml
argument-hint: [content] [--style name] [--quick] [--lang code]
```

## Advanced Patterns

### Partial Execution

Let users run only part of the workflow instead of start-to-finish:

```bash
/slide-deck content.md --outline-only     # Only generate outline
/slide-deck content.md --prompts-only     # Only generate image prompts
/slide-deck slide-deck/topic/ --images-only  # Only generate images
```

In SKILL.md, check the flag and skip to the relevant step:

```markdown
## Step 1: Parse Arguments

$ARGUMENTS

If `--outline-only`: Execute Steps 1-3 only, then output.
If `--images-only`: Skip to Step 7, load existing prompts.
If `--regenerate N`: Skip to Step 7, regenerate only slide N.
Otherwise: Execute full workflow.
```

### Independent Dimensions

Design parameters to be independently combinable — any combination is valid:

```bash
/cover-image article.md --type conceptual --palette warm --rendering flat-vector
/cover-image article.md --quick                # Skip confirmation, full auto
/cover-image article.md --ref style-ref.png    # Use reference image
```

Each dimension (type, palette, rendering) is independent. The user can set any, all, or none.

### Quick Mode

A `--quick` flag that skips confirmation gates is a common and useful pattern:

```markdown
## Step 2: Confirm Options ⚠️ REQUIRED

Unless `--quick` was passed:
- Present options to user
- Wait for confirmation

If `--quick`: Use auto-selected defaults and proceed.
```

This lets power users skip the interactive flow while keeping it safe by default.

### Default Values

Always define sensible defaults for every parameter:

```markdown
## Defaults

- `--style`: auto-detected from content
- `--lang`: same as input content
- `--slides`: 8-12 based on content length
```

This way, `/my-skill content.md` with zero flags still produces good output.
