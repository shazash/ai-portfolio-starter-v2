from src.prompts import JSON_SYSTEM_INSTRUCTIONS, build_product_brief_prompt
from src.parser import parse_and_validate, schema_as_text


def mock_llm(prompt: str, temperature: float) -> str:
    if temperature < 0.3:
        return """{
  "product_name": "RAG Starter Kit",
  "target_audience": "Junior AI developers",
  "value_proposition": "Build structured RAG demos faster.",
  "key_features": ["Prompt templates", "JSON validation"],
  "call_to_action": "Clone and run the demo."
}"""
    return """{
  "product_name": "LLM Portfolio Tool",
  "target_audience": "AI learners",
  "value_proposition": "Turn ideas into structured outputs.",
  "key_features": ["Structured prompts", "Reliable parsing"],
  "call_to_action": "Run the script now."
}"""


def main():
    user_context = "I want a portfolio-ready AI demo."

    prompt = build_product_brief_prompt().format(
        system=JSON_SYSTEM_INSTRUCTIONS,
        user_context=user_context,
        schema=schema_as_text(),
    )

    for temperature in (0.1, 0.8):
        print("=" * 60)
        print(f"Temperature: {temperature}")

        output = mock_llm(prompt, temperature)
        print("Raw output:")
        print(output)

        parsed = parse_and_validate(output)
        print("Parsed object:")
        print(parsed.model_dump())


if __name__ == "__main__":
    main()
