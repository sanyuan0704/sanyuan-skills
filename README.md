# sanyuan-skills

A collection of production-grade agent skills for Claude Code and other AI agent terminals.

<p align="center">
  <img src="https://img.shields.io/badge/Skills-6-blue" alt="6 Skills" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License" />
</p>

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [**Code Review Expert**](./skills/code-review-expert/) | Senior engineer code review covering SOLID, security, performance, error handling | `npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert` |
| [**Sigma**](./skills/sigma/) | 1-on-1 AI tutor based on Bloom's 2-Sigma mastery learning with Socratic questioning | `npx skills add sanyuan0704/sanyuan-skills --path skills/sigma` |
| [**Skill Review**](./skills/skill-review/) | Quality audit for skills: structure, description, workflow, token efficiency, anti-patterns | `npx skills add sanyuan0704/sanyuan-skills --path skills/skill-review` |
| [**Skill Forge**](./skills/skill-forge/) | Meta-skill for creating high-quality skills with 12 battle-tested techniques | `npx skills add sanyuan0704/sanyuan-skills --path skills/skill-forge` |
| [**Wiki Ingest**](./skills/wiki-ingest/) | Compile articles, documents, or notes into a structured, cross-referenced wiki knowledge base | `npx skills add sanyuan0704/sanyuan-skills --path skills/wiki-ingest` |
| [**Book Study**](./skills/book-study/) | Reading coach with knowledge compilation, Socratic mastery testing, spaced repetition, and cross-book querying | `npx skills add sanyuan0704/sanyuan-skills --path skills/book-study` |

## Quick Start

Install any skill with:

```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/<skill-name>
```

Then invoke in your agent terminal:

```bash
/code-review-expert    # Review current git changes
/sigma <topic>         # Start a tutoring session
/skill-review          # Audit an existing skill's quality
/skill-forge           # Create a new skill
/wiki-ingest           # Compile content into a wiki knowledge base
/book-study <book>     # Start a guided reading session
```

## License

MIT
