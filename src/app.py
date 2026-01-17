import os
from src.prompts import JSON_SYSTEM_INSTRUCTIONS, build_product_brief_prompt
from src.parser import parse_and_validate, schema_as_text
from src.providers.openai_provider import OpenAIProvider
from src.providers.watsonx_provider import WatsonxProvider


def get_provider():
    provider = os.environ.get("LLM_PROVIDER", "openai").lower()
    if provider == "watsonx":
        return WatsonxProvider()
    return OpenAIProvider()


def main():
    user_context = "I want a portfolio-ready AI demo."
    prompt = build_product_brief_prompt().format(
        system=JSON_SYSTEM_INSTRUCTIONS,
        user_context=user_context,
        schema=schema_as_text(),
    )

    llm = get_provider()

    for temperature in (0.1, 0.8):
        print("=" * 60)
        print(f"Temperature: {temperature}")

        output = llm.generate(prompt, temperature)
        print("Raw output:")
        print(output)

        parsed = parse_and_validate(output)
        print("Parsed object:")
        print(parsed.model_dump())


if __name__ == "__main__":
    main()

