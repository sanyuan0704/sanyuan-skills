# Writing Killer Skill Descriptions

## Why Description Matters

The `description` field in frontmatter is the ONLY thing Claude reads before deciding to trigger your skill. The SKILL.md body loads AFTER triggering. So "When to Use This Skill" sections in the body are useless for triggering.

Two things description controls:
1. Whether the skill triggers automatically
2. Whether users find it by search

## The Keyword Bombing Technique

List every possible trigger scenario — actions, objects, synonyms, and natural language phrases the user would literally say.

### Four Dimensions of a Great Description

1. **Core capability** — what it does (first sentence)
2. **Action verbs** — what users ask to do
3. **Object nouns** — what users mention
4. **Natural phrases** — what users would literally type

### Excellent Examples

**ui-ux-pro-max:**
```yaml
description: "UI/UX design intelligence. 50 styles, 21 palettes,
50 font pairings, 20 charts, 8 stacks (React, Next.js, Vue, Svelte,
SwiftUI, React Native, Flutter, Tailwind). Actions: plan, build,
create, design, implement, review, fix, improve, optimize, enhance,
refactor, check UI/UX code. Projects: website, landing page,
dashboard, admin panel, e-commerce, SaaS, portfolio, blog, mobile app.
Styles: glassmorphism, claymorphism, minimalism, brutalism..."
```

This is a "trigger keyword net" — no matter what the user says about UI, it hits.

**excalidraw-artist:**
```yaml
description: "Create beautiful, elegant Excalidraw diagrams based on
user intent. Use when user asks to draw, visualize, diagram, sketch,
illustrate concepts, create flowcharts, architecture diagrams, mind maps,
process flows, or any visual representation. Triggers on keywords like
'draw', 'diagram', 'visualize', 'sketch', 'flowchart', 'architecture',
'mind map', 'illustrate'."
```

Explicitly lists trigger keywords in natural language.

### Bad vs Good

```yaml
# Bad — too vague, won't trigger reliably
description: "代码审查工具"

# Good — covers natural language triggers
description: "代码审查与质量分析。当用户说'帮我 review'、'检查代码'、
'审查 PR'、'看看这段代码有没有问题'时使用。支持 Python、JavaScript、
TypeScript、Go、Rust。Actions: review, check, audit, inspect, analyze
code quality, find bugs, security review."
```

```yaml
# Bad — generic
description: "Helps create presentations"

# Good — keyword-rich
description: "Generate professional slide decks from content. Creates
outlines with style instructions, then generates individual slide images.
Use when user asks to 'create slides', 'make a presentation', 'generate
deck', 'slide deck', 'PPT', 'make slides from article', 'turn this into
a presentation'."
```

## Checklist

- [ ] First sentence states core capability
- [ ] 5+ action verbs listed
- [ ] 5+ object nouns / project types listed
- [ ] Natural language trigger phrases included
- [ ] Under 1024 characters
- [ ] No angle brackets (`<` or `>`)
- [ ] All "when to use" info is HERE, not in SKILL.md body

## Key Rule

NEVER put "When to Use This Skill" in the SKILL.md body. The body only helps AFTER triggering — which is too late. All trigger information belongs in the `description` field.
