Simple example:
  given:
    json_schema: |
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
    yaml_snippet: |
      # All about the character
      name: Ford Prefect
      age: 42
      possessions:
      - Towel
    setup: |
      from strictyamljsonschema import load_schema
      from strictyaml import load
      import json
  variations:
    Parse correctly:
      steps:
      - Run:
          code: |
            print(load(yaml_snippet, load_schema(json.loads(json_schema))).data)
          will output: OrderedDict([('name', 'Ford Prefect'), ('age', 42), ('possessions',
            ['Towel'])])
