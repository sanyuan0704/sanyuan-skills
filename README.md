# sanyuan-skills

A collection of production-grade agent skills for Claude Code and other AI agent terminals.

<p align="center">
  <img src="https://img.shields.io/badge/Skills-3-blue" alt="3 Skills" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License" />
  <img src="https://img.shields.io/badge/ci.yml-red" alt="CI" />
</p>

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [**Code Review Expert**](./skills/code-review-expert/) | Senior engineer code review covering SOLID, security, performance, error handling | `npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert` |
| [**Sigma**](./skills/sigma/) | 1-on-1 AI tutor based on Bloom's 2-Sigma mastery learning with Socratic questioning | `npx skills add sanyuan0704/sanyuan-skills --path skills/sigma` |
| [**Skill Forge**](./skills/skill-forge/) | Meta-skill for creating high-quality skills with 12 battle-tested techniques | `npx skills add sanyuan0704/sanyuan-skills --path skills/skill-forge` |

## Quick Start

Install any skill with:

```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/<skill-name>
```

Then invoke in your agent terminal:

```bash
/code-review-expert    # Review current git changes
/sigma <topic>         # Start a tutoring session
/skill-forge           # Create a new skill
```

CI automatically discovers every subfolder under `skills/` and runs the validator/bytecode checks, so new skills are covered without editing the workflow.

## Development Setup (Python helpers)

Some helper scripts (packaging/validation) depend on PyYAML. Set up once per clone:

```bash
python -m venv venv
./venv/Scripts/pip install -r requirements.txt   # Windows
# or
source venv/bin/activate && pip install -r requirements.txt  # macOS/Linux
```

## Customizing project-brain.md (Code Review Expert)

`skills/code-review-expert/references/project-brain.md` ships with sensible defaults (Hexagonal TS/Node stack, Zod/Prisma/Fastify, AppError shape, event naming). Before using on your project:

1) Fill in your actual stack versions and primary libraries.  
2) Update forbidden libraries/anti-patterns to match your org.  
3) Set migration/backward-compat rules and soft-delete policy.  
4) Define your error base class and code conventions.  
5) Confirm event naming + schema versioning rules.  
6) Note coverage targets and test strategy.  
7) Save it to keep reviewers aligned across runs.

## License

MIT
