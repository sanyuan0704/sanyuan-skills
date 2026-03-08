#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template with best-practice structure.

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: "[TODO: Write a keyword-rich description. Include: (1) core capability in first sentence, (2) 5+ action verbs users might say, (3) 5+ object nouns, (4) natural language trigger phrases. See references/description-guide.md for examples. ALL trigger info goes HERE, not in the body.]"
---

# {skill_title}

[TODO: Write your Iron Law here. Ask: "What is the ONE mistake the model will most likely make?" Then write an unbreakable rule to prevent it.]

IRON LAW: [TODO: e.g., "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST."]

## Workflow

Copy this checklist and check off items as you complete them:

```
{skill_title} Progress:

- [ ] Step 1: [TODO: First step] ⚠️ REQUIRED
  - [ ] 1.1 [TODO: Sub-step]
  - [ ] 1.2 [TODO: Sub-step]
- [ ] Step 2: Confirm with user ⚠️ REQUIRED
- [ ] Step 3: [TODO: Core operation]
- [ ] Step 4: [TODO: Output / delivery]
```

## Step 1: [TODO: First Step]

[TODO: Use question-style instructions, not vague directives.
Instead of "Check for problems", write "Ask: What happens if this value is null?"]

## Step 2: Confirm ⚠️ REQUIRED

[TODO: Present findings/plan to user before proceeding. Options:]
- Proceed with all?
- Only high-priority items?
- Select specific items?
- View only, no changes?

⚠️ Do NOT proceed without user confirmation.

## Step 3: [TODO: Core Operation]

[TODO: The main work of the skill. Load references as needed:]
- Load references/[TODO].md for [specific purpose]

## Step 4: [TODO: Output]

[TODO: Define output format and structure]

## Anti-Patterns

[TODO: List what the model should NOT do. Ask: "What would Claude's lazy default look like?"]
- [TODO: e.g., Don't use purple/blue gradients by default]
- [TODO: e.g., Don't add unnecessary try-catch blocks]

## Pre-Delivery Checklist

[TODO: Add concrete, verifiable checks — not "ensure quality" but specific items]
- [ ] [TODO: e.g., No placeholder text remaining (TODO, FIXME)]
- [ ] [TODO: e.g., All generated code runs without errors]
- [ ] [TODO: e.g., Output matches requested format]
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with best-practice template.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    ).lstrip('\n')

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("Created SKILL.md")
    except Exception as e:
        print(f"Error creating SKILL.md: {e}")
        return None

    # Create resource directories (empty — user fills as needed)
    for dirname in ('scripts', 'references', 'assets'):
        (skill_dir / dirname).mkdir(exist_ok=True)
        print(f"Created {dirname}/")

    print(f"\nSkill '{skill_name}' initialized at {skill_dir}")
    print("\nNext steps:")
    print("1. Fill in all [TODO] items in SKILL.md")
    print("2. Write your description using the keyword bombing technique")
    print("3. Add scripts/, references/, assets/ as needed")
    print("4. Delete any empty resource directories you don't need")
    print("5. Run package_skill.py when ready")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print()
        print("Skill name requirements:")
        print("  - Hyphen-case (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 64 characters")
        print()
        print("Examples:")
        print("  init_skill.py my-skill --path ./skills")
        print("  init_skill.py code-reviewer --path /custom/location")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"Initializing skill: {skill_name}")
    print(f"Location: {path}")
    print()

    result = init_skill(skill_name, path)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
