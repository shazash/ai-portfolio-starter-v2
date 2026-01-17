import os
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference


class WatsonxProvider:
    def __init__(self, model_id: str = "meta-llama/llama-3-3-70b-instruct"):
        api_key = os.environ.get("WATSONX_API_KEY")
        url = os.environ.get("WATSONX_URL")
        project_id = os.environ.get("WATSONX_PROJECT_ID")

        if not (api_key and url and project_id):
            raise RuntimeError("Missing WATSONX_API_KEY / WATSONX_URL / WATSONX_PROJECT_ID.")

        self.project_id = project_id
        self.model = ModelInference(
            model_id=model_id,
            credentials=Credentials(api_key=api_key, url=url),
            project_id=project_id,
        )

    def generate(self, prompt: str, temperature: float) -> str:
        params = {
            "temperature": temperature,
            "max_new_tokens": 300,
        }
        result = self.model.generate_text(prompt=prompt, params=params)
        return result
