# Skill Forge

Create high-quality Claude Code skills instead of AI-generated slop.

## The Problem

Most skills are just a big markdown file dumped into SKILL.md — no structure, no workflow, no quality control. The model reads a wall of text, loses focus on what matters, and produces inconsistent output.

Skill Forge fixes this by teaching you **12 battle-tested techniques** for skill design: how to manage context efficiently, how to guide the model step-by-step, and how to prevent it from taking shortcuts.

## What's Inside

| Technique | What It Solves |
|-----------|---------------|
| Progressive Loading | Context bloat — keep SKILL.md lean, load details on demand |
| Keyword Bombing | Skills that never trigger — write descriptions that actually match user intent |
| Workflow Checklist | Inconsistent execution — give the model a trackable path with ⚠️/⛔ markers |
| Script Encapsulation | Wasted tokens — wrap deterministic ops in scripts (zero context cost) |
| Question-Style Instructions | Vague output — ask specific questions instead of abstract directives |
| Confirmation Gates | Runaway execution — force the model to pause before critical operations |
| Pre-Delivery Checklist | Quality gaps — add concrete, verifiable checks before output |
| Parameter System | Inflexibility — support `--flags`, partial execution, `--quick` mode |
| Reference Organization | Loading irrelevant context — organize by domain, load only what's needed |
| CLI + Skill Pattern | MCP overhead — replace MCP Servers with CLI tools |
| Iron Law | Model shortcuts — set one unbreakable rule the model can never violate |
| Anti-Pattern Documentation | Default AI behavior — explicitly list what NOT to do |

## Install

```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/skill-forge
```

## Usage

```
/skill-forge
```

Follow the guided workflow — from understanding requirements to packaging a distributable `.skill` file.

## Structure

```
skill-forge/
├── SKILL.md                          # Core workflow (<250 lines)
├── scripts/
│   ├── init_skill.py                 # Initialize new skill from template
│   ├── package_skill.py              # Package into .skill file
│   └── quick_validate.py             # Validate structure and frontmatter
└── references/                       # Loaded on demand, not upfront
    ├── description-guide.md          # How to write trigger-rich descriptions
    ├── workflow-patterns.md          # Checklists, confirmation gates, pre-delivery
    ├── writing-techniques.md         # Question prompting, iron laws, anti-patterns
    ├── architecture-guide.md         # Progressive loading, scripts, CLI+Skill
    ├── parameter-system.md           # $ARGUMENTS, flags, partial execution
    └── output-patterns.md            # Templates, examples, delivery checklists
```

## License

MIT
