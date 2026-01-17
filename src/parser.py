from typing import List
from pydantic import BaseModel, Field, ValidationError, ConfigDict


class ProductBrief(BaseModel):
    model_config = ConfigDict(extra="forbid")
    product_name: str = Field(min_length=2, max_length=80)
    target_audience: str = Field(min_length=3, max_length=120)
    value_proposition: str = Field(min_length=5, max_length=200)
    key_features: List[str]
    call_to_action: str = Field(min_length=5, max_length=120)


def schema_as_text() -> str:
    return """{
  "product_name": "string",
  "target_audience": "string",
  "value_proposition": "string",
  "key_features": ["string", "string"],
  "call_to_action": "string"
}"""


def parse_and_validate(json_text: str) -> ProductBrief:
    try:
        return ProductBrief.model_validate_json(json_text)
    except ValidationError as e:
        raise ValueError(f"Invalid JSON output: {e}") from e
