from strictyaml import Map, MapPattern, Optional
from strictyaml import Str, Int, Seq, Enum, Any, as_document

JSONSCHEMA_TYPE_SNIPPET = {
    "type": Enum(["object", "integer", "string", "array"]),
    Optional("required"): Seq(Str()),
    Optional("properties"): MapPattern(Str(), Any()),
    Optional("items"): Any(),
}

JSONSCHEMA_SCHEMA = Map(JSONSCHEMA_TYPE_SNIPPET)


def get_schema(snippet):
    if snippet['type'] == "integer":
        return Int()
    elif snippet['type'] == "string":
        return Str()
    elif snippet['type'] == "array":
        return Seq(get_schema(snippet["items"]))
    elif snippet['type'] == "object":
        map_schema = {}
        for key, subschema in snippet['properties'].items():
            if key in snippet.get('required', []):
                map_schema[Optional(key)] = get_schema(subschema)
            else:
                map_schema[key] = get_schema(subschema)
        return Map(map_schema)


def load_schema(json_schema):
    return get_schema(as_document(json_schema, JSONSCHEMA_SCHEMA).data)
