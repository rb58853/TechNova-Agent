"""
Prompt Selection
"""

import yaml
from pathlib import Path

system_prompts: dict = {}
prompts_dir = Path(__file__).parent

# Load all YAML files in the directory
for yaml_file in prompts_dir.glob("*.yaml"):
    try:
        with open(yaml_file) as f:
            prompts = yaml.safe_load(f)
            if prompts:
                system_prompts.update(prompts)
    except:
        pass


def get_system_prompt(prompt_name: str) -> str:
    return system_prompts.get(prompt_name, "")
