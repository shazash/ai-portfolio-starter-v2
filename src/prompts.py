from dataclasses import dataclass


@dataclass(frozen=True)
class PromptTemplate:
    template: str

    def format(self, **kwargs) -> str:
        return self.template.format(**kwargs)


JSON_SYSTEM_INSTRUCTIONS = """You are a strict JSON generator.
Return ONLY valid JSON.
Do not include markdown.
Do not add extra keys.
"""


def build_product_brief_prompt() -> PromptTemplate:
    return PromptTemplate(
        template=(
            "{system}\n"
            "Task: Generate a product brief for a LinkedIn portfolio demo.\n"
            "User context: {user_context}\n"
            "Output schema (JSON):\n"
            "{schema}\n"
        )
    )
