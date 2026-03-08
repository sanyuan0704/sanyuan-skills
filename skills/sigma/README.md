# Sigma

Personalized 1-on-1 AI tutor agent skill. Based on Bloom's 2-Sigma mastery learning — the finding that students tutored one-on-one with mastery methods perform **2 standard deviations** above conventional classroom students.

Sigma guides you through any topic with Socratic questioning, adaptive pacing, and rich visual output (HTML dashboards, Excalidraw concept maps, generated images).

Compatible with any AI agent terminal: **Claude Code** / **Cursor** / **Trae** / **CodeX** / **Windsurf** and more.

<p align="center">
  <img src="https://img.shields.io/badge/Agent_Skill-Tutor-blue" alt="Agent Skill" />
  <img src="https://img.shields.io/badge/Method-Bloom's_2--Sigma-green" alt="Bloom's 2-Sigma" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License" />
</p>

## Installation

```bash
npx skills add sanyuan0704/sanyuan-skills --path skills/sigma
```

## Features

- **Socratic Questioning** — Never gives answers directly; guides you to discover them yourself
- **Mastery Learning** — Advances to the next concept only when you demonstrate ≥80% understanding via calibrated rubric scoring
- **Misconception Tracking** — Identifies wrong mental models behind incorrect answers, designs counter-examples to dismantle them, tracks resolution
- **Spaced Repetition** — SM-2 inspired review scheduling on resume; mastered concepts are re-tested at increasing intervals to fight the forgetting curve
- **Interleaving** — Mixes questions about previously mastered concepts into the current learning flow, improving long-term retention by ~43%
- **Practice Phase** — Requires learners to DO something (write code, design, explain) before a concept is marked mastered — understanding ≠ ability
- **Self-Assessment Calibration** — Detects fluency illusion by comparing learner's self-assessment with rubric scores
- **Adaptive Pacing** — Speeds up when you're flying, slows down when you're struggling
- **Visual Roadmap** — Live HTML dashboard tracking your progress through every concept
- **Concept Maps** — Excalidraw diagrams showing relationships between topics
- **Cross-Topic Learner Profile** — Remembers your learning style, misconception patterns, and strengths across different topics
- **Session Persistence** — Save and resume learning sessions anytime
- **Multilingual** — Follows your language automatically; technical terms stay in English with translation

## Usage

After installation, invoke with:

```bash
/sigma Python decorators
/sigma 量子力学 --level beginner
/sigma React hooks --level intermediate --lang zh
/sigma linear algebra --resume    # Resume previous session
```

### Arguments

| Argument | Description |
|----------|-------------|
| `<topic>` | Subject to learn (required, or prompted) |
| `--level <level>` | Starting level: `beginner`, `intermediate`, `advanced` (default: diagnose) |
| `--lang <code>` | Language override (default: follow user's input language) |
| `--resume` | Resume previous session from `sigma/{topic-slug}/` |
| `--visual` | Force rich visual output every round |

## How It Works

```
Input → Parse Topic → Diagnose Level → Build Roadmap → Tutor Loop → Session End
                          ↑                                  |
                          |     (mastery < 80%)              |
                          +----------------------------------+
```

### 1. Diagnose

Sigma starts by probing your current understanding with 2-3 diagnostic questions — mixing multiple choice and open-ended — to calibrate exactly where you are.

### 2. Build Roadmap

Decomposes the topic into 5-15 atomic concepts ordered by dependency, then generates a visual HTML roadmap showing your learning path.

### 3. Tutor Loop

For each concept:
- **Introduce** with a question, not a lecture
- **Question cycle** alternating structured choices, open-ended questions, and interleaving with past concepts
- **Misconception tracking** — wrong answers are diagnosed for underlying wrong mental models, counter-examples are designed to dismantle them
- **Respond adaptively** — harder follow-ups for correct answers, simpler sub-questions for gaps
- **Visual aids** when they genuinely help (Excalidraw diagrams, HTML walkthroughs, generated images)
- **Calibrated mastery check** after 3-5 rounds — rubric-based scoring + learner self-assessment to detect fluency illusion
- **Practice phase** — hands-on task to cross the knowing-doing gap before marking mastered

### 4. Session Output

```
sigma/
├── learner-profile.md          # Cross-topic learner model (persists across topics)
└── {topic-slug}/
    ├── session.md              # Learning state, mastery scores, misconceptions, review schedule
    ├── roadmap.html            # Visual learning roadmap (updated every round)
    ├── concept-map/            # Excalidraw concept maps
    ├── visuals/                # HTML explanations, diagrams, images
    └── summary.html            # Session summary (at milestones or end)
```

## Pedagogy

Based on seven proven principles from cognitive science:

| Principle | Research | Implementation |
|-----------|----------|----------------|
| **Bloom's 2-Sigma** | Bloom 1984 | 1-on-1 tutoring + mastery gating at 80% via calibrated rubric |
| **Socratic Method** | Classical | Questions only — never lecture, never hand-wave |
| **Spaced Repetition** | Ebbinghaus 1885, SM-2 | Review mastered concepts at increasing intervals on resume |
| **Interleaving** | Rohrer & Taylor 2007 | Mix old concepts into current question flow (+43% retention) |
| **Misconception Dismantling** | Vosniadou 2013, Chi 2005 | Counter-example method to dislodge wrong mental models |
| **Deliberate Practice** | Ericsson 1993 | Hands-on practice phase before marking mastered |
| **Metacognition** | Bjork 1994 | Self-assessment calibration to detect fluency illusion |

Question types include: predict, compare, debug, extend, teach-back, and connect — keeping engagement high through variety.

## Structure

```
sigma/
├── SKILL.md                    # Core skill definition
├── README.md                   # This file
└── references/
    ├── pedagogy.md             # Bloom's 2-Sigma theory, question design, mastery criteria
    ├── html-templates.md       # Roadmap, summary, and visual HTML templates
    └── excalidraw.md           # Excalidraw diagram guide, element format, color palette
```

## References

- **pedagogy.md** — Bloom's 2-Sigma theory, Socratic questioning, calibrated mastery scoring, misconception handling, spaced repetition, interleaving, deliberate practice
- **html-templates.md** — Premium dark UI templates for roadmap, summary, and visual explanations (glassmorphism, micro-animations)
- **excalidraw.md** — Excalidraw HTML template, element types, color palette, layout patterns for concept maps and flowcharts

## License

MIT
