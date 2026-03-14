# sanyuan-skills

A curated collection of production-grade AI agent skills designed for Claude Code and other AI agent terminals. These skills provide specialized capabilities for code review, tutoring, and skill development, each with comprehensive reference materials and battle-tested approaches.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Stars-2658-blue?style=flat&logo=github" alt="GitHub Stars" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat" alt="MIT License" />
  <img src="https://img.shields.io/badge/Skills-2-green?style=flat" alt="Skills Count" />
</p>

## ✨ Features

- **🔍 Expert Code Review**: Comprehensive code analysis covering SOLID principles, security, performance, and error handling
- **👨‍🏫 AI Tutoring**: 1-on-1 personalized learning based on Bloom's 2-Sigma mastery learning methodology
- **📚 Rich References**: Detailed checklists and guidelines for each skill domain
- **🤖 Agent Integration**: Ready-to-use agent configurations for seamless deployment
- **🎯 Production-Ready**: Battle-tested skills with proven effectiveness

## 🚀 Skills

| Skill | Description | Install Command |
|-------|-------------|----------------|
| [**Code Review Expert**](./skills/code-review-expert/) | Senior-level code review covering SOLID principles, security vulnerabilities, performance optimization, and robust error handling | `npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert` |
| [**Sigma**](./skills/sigma/) | 1-on-1 AI tutor implementing Bloom's 2-Sigma mastery learning with Socratic questioning methodology | `npx skills add sanyuan0704/sanyuan-skills --path skills/sigma` |

## 📦 Installation

### Prerequisites
- Node.js and npm installed
- Access to an AI agent terminal (Claude Code, etc.)

### Install Individual Skills

```bash
# Install Code Review Expert skill
npx skills add sanyuan0704/sanyuan-skills --path skills/code-review-expert

# Install Sigma tutoring skill
npx skills add sanyuan0704/sanyuan-skills --path skills/sigma
```

### Clone Repository
```bash
git clone https://github.com/sanyuan0704/sanyuan-skills.git
cd sanyuan-skills
```

## 💡 Usage

### Code Review Expert
The Code Review Expert skill provides comprehensive code analysis with focus on:

- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Security Analysis**: Vulnerability detection and security best practices
- **Performance Optimization**: Code efficiency and performance bottlenecks
- **Error Handling**: Robust exception handling and boundary condition checks

Reference materials include detailed checklists for each review area.

### Sigma Tutor
The Sigma skill implements advanced tutoring methodologies:

- **Bloom's 2-Sigma Learning**: Personalized mastery-based learning approach
- **Socratic Questioning**: Guided discovery through strategic questioning
- **Adaptive Teaching**: Adjusts to individual learning pace and style

Includes pedagogical references and teaching templates.

## 📁 Repository Structure

```
sanyuan-skills/
├── skills/
│   ├── code-review-expert/
│   │   ├── agents/
│   │   │   └── agent.yaml
│   │   ├── references/
│   │   │   ├── code-quality-checklist.md
│   │   │   ├── security-checklist.md
│   │   │   └── solid-checklist.md
│   │   ├── README.md
│   │   └── SKILL.md
│   └── sigma/
│       ├── references/
│       │   ├── excalidraw.md
│       │   ├── html-templates.md
│       │   └── pedagogy.md
│       ├── README.md
│       └── SKILL.md
├── LICENSE
└── README.md
```

## 🤝 Contributing

We welcome contributions to improve existing skills or add new ones! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Follow the existing skill structure and documentation patterns
4. Include comprehensive reference materials and checklists
5. Test your skill thoroughly
6. Submit a pull request

### Skill Development Guidelines
- Each skill should have a dedicated directory under `/skills/`
- Include `README.md`, `SKILL.md`, and relevant reference materials
- Provide agent configuration files where applicable
- Follow the established documentation format

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Documentation improved by [Codec8](https://codec8.com) — AI-powered docs for GitHub repos. [Generate docs for your repo →](https://codec8.com)*