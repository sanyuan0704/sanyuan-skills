#!/usr/bin/env python3
"""
Quick validation script for skills.
Checks SKILL.md frontmatter and agent interface files.
"""

import sys
import re
import yaml
from pathlib import Path
from typing import List, Tuple


def _error_list() -> List[str]:
    return []


def validate_skill(skill_path: Path) -> Tuple[bool, str]:
    """Basic validation of a skill."""
    errors = _error_list()
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
        return False, "; ".join(errors)

    # Read and validate frontmatter
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        errors.append("No YAML frontmatter found")
        return False, "; ".join(errors)

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        errors.append("Invalid frontmatter format")
        return False, "; ".join(errors)

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            errors.append("Frontmatter must be a YAML dictionary")
            return False, "; ".join(errors)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")
        return False, "; ".join(errors)

    # Define allowed properties
    ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata", "argument-hint"}

    # Check for unexpected properties
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        errors.append(
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # Check required fields
    if "name" not in frontmatter:
        errors.append("Missing 'name' in frontmatter")
    if "description" not in frontmatter:
        errors.append("Missing 'description' in frontmatter")

    # Validate name
    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        errors.append(f"Name must be a string, got {type(name).__name__}")
    else:
        name = name.strip()
        if name:
            if not re.match(r"^[a-z0-9-]+$", name):
                errors.append("Name should be hyphen-case (lowercase letters, digits, and hyphens only)")
            if name.startswith("-") or name.endswith("-") or "--" in name:
                errors.append("Name cannot start/end with hyphen or contain consecutive hyphens")
            if len(name) > 64:
                errors.append(f"Name is too long ({len(name)} characters). Maximum is 64 characters.")

    # Validate description
    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        errors.append(f"Description must be a string, got {type(description).__name__}")
    else:
        description = description.strip()
        if description:
            if "<" in description or ">" in description:
                errors.append("Description cannot contain angle brackets (< or >)")
            if len(description) > 1024:
                errors.append(f"Description is too long ({len(description)} characters). Maximum is 1024 characters.")

    # Validate agent interface files (if present)
    agent_dir = skill_path / "agents"
    if agent_dir.exists() and agent_dir.is_dir():
        agent_files = list(agent_dir.glob("*.yml")) + list(agent_dir.glob("*.yaml"))
        if not agent_files:
            errors.append("agents/ directory exists but contains no *.yml/*.yaml files")
        for agent_file in agent_files:
            try:
                data = yaml.safe_load(agent_file.read_text(encoding="utf-8"))
            except yaml.YAMLError as e:
                errors.append(f"{agent_file.name}: invalid YAML ({e})")
                continue
            if not isinstance(data, dict):
                errors.append(f"{agent_file.name}: top-level must be a mapping")
                continue
            interface = data.get("interface")
            if not isinstance(interface, dict):
                errors.append(f"{agent_file.name}: missing 'interface' mapping")
                continue
            required_fields = ("display_name", "short_description", "default_prompt")
            for field in required_fields:
                value = interface.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{agent_file.name}: 'interface.{field}' must be a non-empty string")
            # Allow extra keys but flag empty strings
            for key, value in interface.items():
                if isinstance(value, str) and not value.strip():
                    errors.append(f"{agent_file.name}: 'interface.{key}' is empty")

    if errors:
        return False, "; ".join(errors)

    return True, "Skill and agents are valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
