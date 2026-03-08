# sanyuan-skills

A collection of production-grade agent skills for Claude Code and other AI agent terminals.

<p align="center">
  <img src="https://img.shields.io/badge/Skills-3-blue" alt="3 Skills" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License" />
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

## License

MIT
