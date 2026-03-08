# Skill Architecture Guide

## Progressive Loading

### The 500-Line Rule

SKILL.md must stay under 500 lines. Everything beyond that goes into `references/`.

Why? The context window is shared with system prompts, conversation history, user input, and other skill metadata. A bloated SKILL.md crowds out everything else.

**Bad:** A 2000-line SKILL.md with API docs, examples, and FAQ all in one file. The model reads all of it, and the truly important instructions get buried.

**Good:** A 150-line SKILL.md with clear workflow steps. Each step says "Load references/xxx.md" only when needed.

### Three-Level Loading

1. **Metadata (name + description)** — Always in context (~100 words)
2. **SKILL.md body** — Loaded when skill triggers (<500 lines)
3. **Bundled resources** — Loaded on demand (unlimited)

### Load-on-Demand Pattern

In SKILL.md, reference files only at the step where they're needed:

```markdown
## Step 3: Security Review

Load references/security-checklist.md and check each item against the code.
```

The model reads security-checklist.md only when it reaches Step 3 — not at the beginning.

### Progressive Disclosure Patterns

**Pattern 1: High-level guide with references**

```markdown
# PDF Processing

## Quick start
Extract text with pdfplumber:
[code example]

## Advanced features
- **Form filling**: See references/forms.md for complete guide
- **API reference**: See references/api.md for all methods
```

Claude loads forms.md or api.md only when needed.

**Pattern 2: Conditional details**

```markdown
# DOCX Processing

## Creating documents
Use docx-js for new documents. See references/docx-js.md.

## Editing documents
For simple edits, modify the XML directly.
**For tracked changes**: See references/redlining.md
```

Claude reads redlining.md only when the user needs tracked changes.

## Reference Organization

### Organize by Domain, Not by Type

```
# Bad — organized by type (everything in each folder gets loaded together)
references/
├── checklists/
├── templates/
└── examples/

# Good — organized by domain (only relevant domain gets loaded)
references/
├── palettes/          # 9 color schemes, one per file
├── renderings/        # 6 rendering styles, one per file
├── dimensions/        # Style dimensions
├── config/            # Configuration
└── workflow/          # Workflow details
```

When the user picks a specific palette, the model loads only that one file — not all 9.

### Multi-Framework Skills

```
cloud-deploy/
├── SKILL.md (workflow + provider selection)
└── references/
    ├── aws.md         # Loaded only when user chooses AWS
    ├── gcp.md         # Loaded only when user chooses GCP
    └── azure.md       # Loaded only when user chooses Azure
```

### Rules

1. **One level of nesting only.** All references reachable directly from SKILL.md.
2. **Clear "when to load" instructions.** SKILL.md says when each reference is needed.
3. **Large files (>100 lines) get a TOC** at the top so the model can preview scope.
4. **No duplication.** Information lives in SKILL.md OR references, not both.

## Script Encapsulation

### When to Use Scripts

Ask: "Is this operation deterministic and repeatable?" If yes → script it.

Examples:
- PDF rotation → `scripts/rotate_pdf.py`
- Design database search → `scripts/search.py`
- Image merging → `scripts/merge_images.py`
- File format conversion → `scripts/convert.py`

### Key Benefit: No Context Cost

Scripts execute without being loaded into context. The model only needs to know:
1. The script exists
2. What arguments it takes
3. What it returns

This saves massive context compared to the model writing the same code from scratch each time.

### Document Scripts Minimally in SKILL.md

```markdown
## Available Scripts

### scripts/search.py
Search the design database for matching styles.
Usage: `python3 scripts/search.py "<query>" --domain <color|font|layout>`
Returns: JSON array of matching entries with name, values, and usage notes.
```

The model calls it via Bash without reading the script's source code.

### Script Testing

Added scripts must be tested by actually running them. If there are many similar scripts, test a representative sample.

## CLI + Skill Pattern (MCP Alternative)

For capabilities that would traditionally require an MCP Server, consider: CLI tool + Skill.

### How It Works

Instead of an MCP Server with 20+ tool definitions in context, use:
- A CLI tool with clear commands
- A SKILL.md that teaches the model how to use it

### Example — Browser Automation

```bash
agent-browser open https://example.com
agent-browser snapshot -i
agent-browser click @e1
agent-browser fill @e2 "text"
```

SKILL.md lists the command reference. The model calls them via Bash.
Context savings: up to 93% compared to MCP approach.

### Security: Restrict Allowed Tools

Use `allowed-tools` in frontmatter to restrict what the skill can execute:

```yaml
allowed-tools: Bash(agent-browser:*)
```

The skill can ONLY run commands starting with `agent-browser` — nothing else.

### When to Choose CLI + Skill over MCP

- The tool has a clean command-line interface
- You want to minimize context usage
- The tool doesn't need bidirectional streaming
- You want simpler deployment (no server to run)

## What NOT to Include in a Skill

A skill should only contain files that directly support its functionality. Do NOT create:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- Any user-facing documentation

The skill is for an AI agent to do the job — not for humans to read about it.
