import os
import streamlit as st

from src.prompts import JSON_SYSTEM_INSTRUCTIONS, build_product_brief_prompt
from src.parser import parse_and_validate, schema_as_text
from src.providers.openai_provider import OpenAIProvider
from src.providers.watsonx_provider import WatsonxProvider


def get_provider(provider_name: str):
    if provider_name == "watsonx":
        return WatsonxProvider()
    return OpenAIProvider()


st.title("LLM Prompt Templates + JSON Parser Demo")

provider_name = st.selectbox("Provider", ["openai", "watsonx"])
temperature = st.slider("Temperature", 0.0, 1.0, 0.2, 0.1)
user_context = st.text_area("User context", "I want a portfolio-ready AI demo.")

prompt = build_product_brief_prompt().format(
    system=JSON_SYSTEM_INSTRUCTIONS,
    user_context=user_context,
    schema=schema_as_text(),
)

st.subheader("Prompt preview")
st.code(prompt)

if st.button("Generate JSON"):
    try:
        llm = get_provider(provider_name)
        output = llm.generate(prompt, temperature)
        st.subheader("Raw output")
        st.code(output)

        parsed = parse_and_validate(output)
        st.subheader("Parsed JSON")
        st.json(parsed.model_dump())
        st.success("Valid JSON output.")
    except Exception as e:
        st.error(str(e))
