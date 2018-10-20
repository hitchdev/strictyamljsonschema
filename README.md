# StrictYAMLJSONSchema

Translate JSON schemas in to StrictYAML schema.


Simple example:

```json
{
    "type": "object",
    "properties": {
        "age": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "possessions": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["age", "name", "possession"]
}

```


```yaml
# All about the character
name: Ford Prefect
age: 42
possessions:
- Towel

```


```python
from strictyamljsonschema import load_schema
from strictyaml import load
import json

```





Parse correctly:


```python
print(load(yaml_snippet, load_schema(json.loads(json_schema))).data)

```

```yaml
OrderedDict([('name', 'Ford Prefect'), ('age', 42), ('possessions', ['Towel'])])
```






## Install

```sh
$ pip install strictyamljsonschema
```