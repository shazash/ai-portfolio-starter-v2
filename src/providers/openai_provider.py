import os
from openai import OpenAI


class OpenAIProvider:
    def __init__(self, model: str = "gpt-4.1-mini"):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = model

    def generate(self, prompt: str, temperature: float) -> str:
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("Missing OPENAI_API_KEY environment variable.")

        resp = self.client.responses.create(
            model=self.model,
            input=prompt,
            temperature=temperature,
        )
        # The SDK returns output items; for a simple text-only response, use output_text.
        return resp.output_text
