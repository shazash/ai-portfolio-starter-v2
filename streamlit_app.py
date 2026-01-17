import streamlit as st

from src.prompts import JSON_SYSTEM_INSTRUCTIONS, build_product_brief_prompt
from src.parser import parse_and_validate, schema_as_text


def mock_llm(prompt: str, temperature: float) -> str:
    # نفس فكرة المشروع: قابل للتشغيل بدون مفاتيح
    if temperature <= 0.2:
        return """{
  "product_name": "RAG Starter Kit",
  "target_audience": "Junior AI developers",
  "value_proposition": "Build structured RAG demos faster with reliable JSON outputs.",
  "key_features": ["Prompt templates", "JSON validation", "Retrieval-ready structure"],
  "call_to_action": "Clone the repo and run the demo."
}"""
    return """{
  "product_name": "LLM Portfolio Tool",
  "target_audience": "AI learners building portfolio projects",
  "value_proposition": "Turn ideas into structured outputs that are easy to validate and use.",
  "key_features": ["Structured prompts", "Schema validation", "Parameter comparison"],
  "call_to_action": "Run the app and generate your first brief."
}"""


st.set_page_config(page_title="LLM JSON Parser Demo", layout="wide")
st.title("LLM Prompt Templates + JSON Output Parser")

st.write(
    "This demo generates **JSON-only** output and validates it against a schema. "
    "It also shows how output varies with **temperature**."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Inputs")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.2, 0.1)
    user_context = st.text_area(
        "User context",
        "I want a portfolio-ready AI demo showcasing prompt templates and JSON parsing.",
        height=120,
    )
    run = st.button("Generate JSON")

with col2:
    st.subheader("Schema (expected JSON)")
    st.code(schema_as_text(), language="json")

prompt = build_product_brief_prompt().format(
    system=JSON_SYSTEM_INSTRUCTIONS,
    user_context=user_context,
    schema=schema_as_text(),
)

st.subheader("Prompt preview")
st.code(prompt)

if run:
    st.subheader("Raw model output")
    raw = mock_llm(prompt, temperature)
    st.code(raw, language="json")

    st.subheader("Parsed & validated output")
    try:
        parsed = parse_and_validate(raw)
        st.json(parsed.model_dump())
        st.success("Valid JSON output (schema passed).")
    except Exception as e:
        st.error(f"Validation failed: {e}")
