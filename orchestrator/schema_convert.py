"""Best-effort JSON Schema (what MCP tools declare) -> google-genai Schema
converter. MCP tool.inputSchema is standard JSON Schema; genai.types.Schema
uses an enum for `type` and a slightly narrower feature set. This covers the
common cases (object/string/number/integer/boolean/array, nested objects,
enum, required). If a Neo4j MCP tool ever exposes something exotic
(oneOf/anyOf, $ref, etc.) extend this function.
"""
from __future__ import annotations

from google.genai import types

_TYPE_MAP = {
    "string": types.Type.STRING,
    "number": types.Type.NUMBER,
    "integer": types.Type.INTEGER,
    "boolean": types.Type.BOOLEAN,
    "array": types.Type.ARRAY,
    "object": types.Type.OBJECT,
}


def json_schema_to_genai_schema(schema: dict) -> types.Schema:
    json_type = schema.get("type", "object")
    kwargs: dict = {"type": _TYPE_MAP.get(json_type, types.Type.STRING)}

    if description := schema.get("description"):
        kwargs["description"] = description
    if enum := schema.get("enum"):
        kwargs["enum"] = enum

    if json_type == "object":
        properties = schema.get("properties") or {}
        if properties:
            kwargs["properties"] = {
                key: json_schema_to_genai_schema(value) for key, value in properties.items()
            }
        if required := schema.get("required"):
            kwargs["required"] = required

    if json_type == "array" and (items := schema.get("items")):
        kwargs["items"] = json_schema_to_genai_schema(items)

    return types.Schema(**kwargs)
