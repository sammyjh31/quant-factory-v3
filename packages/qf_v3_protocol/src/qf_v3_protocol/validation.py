from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError as JsonSchemaValidationError

SCHEMA_DIR = Path(__file__).resolve().parent / "schemas"


class ValidationError(Exception):
    """Raised when a protocol record fails schema validation."""


@dataclass(frozen=True)
class ValidationResult:
    path: Path
    schema_name: str
    valid: bool


@lru_cache
def load_schema(schema_name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / f"{schema_name}.schema.json"
    if not path.exists():
        raise ValidationError(f"Unknown protocol schema: {schema_name}")
    return json.loads(path.read_text())


def _iter_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        return [payload]
    raise ValidationError("Protocol payload must be a JSON object or list of objects")


def validate_record(record: dict[str, Any]) -> dict[str, Any]:
    schema_name = record.get("schema_name")
    if not isinstance(schema_name, str):
        raise ValidationError("Protocol record is missing string field: schema_name")
    schema = load_schema(schema_name)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(record), key=lambda error: list(error.path))
    if errors:
        details = "; ".join(_format_error(error) for error in errors[:5])
        raise ValidationError(f"{schema_name} validation failed: {details}")
    return record


def validate_path(path: Path) -> list[ValidationResult]:
    payload = json.loads(path.read_text())
    results: list[ValidationResult] = []
    for record in _iter_records(payload):
        validate_record(record)
        results.append(ValidationResult(path=path, schema_name=record["schema_name"], valid=True))
    return results


def _format_error(error: JsonSchemaValidationError) -> str:
    location = ".".join(str(part) for part in error.path)
    if not location:
        location = "<root>"
    return f"{location}: {error.message}"
