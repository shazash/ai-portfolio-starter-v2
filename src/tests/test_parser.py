import pytest
from src.parser import parse_and_validate

def test_invalid_json():
    with pytest.raises(ValueError):
        parse_and_validate("NOT JSON")

def test_missing_field():
    bad = """{
      "product_name": "X",
      "target_audience": "Y",
      "value_proposition": "Z",
      "key_features": ["a","b"]
    }"""
    with pytest.raises(ValueError):
        parse_and_validate(bad)

def test_extra_key_forbidden():
    bad = """{
      "product_name": "X",
      "target_audience": "Y",
      "value_proposition": "Z",
      "key_features": ["a","b"],
      "call_to_action": "Do it",
      "extra": "nope"
    }"""
    with pytest.raises(ValueError):
        parse_and_validate(bad)
