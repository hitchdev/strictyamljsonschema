{% if readme -%}
# StrictYAMLJSONSchema
{%- else -%}
---
title: StrictYAMLJSONSchema
---
{% endif %}

Translate JSON schemas in to StrictYAML schema.

{% for story in quickstart %}
{{ story.name }}:
{% if 'json_schema' in story.data['given'] %}
```json
{{ story.given['json_schema'] }}
```
{% endif %}
{% if 'yaml_snippet' in story.data['given'] %}
```yaml
{{ story.given['yaml_snippet'] }}
```
{% endif %}
{% if 'setup' in story.data['given'] %}
```python
{{ story.given['setup'] }}
```
{% endif %}


{% for variation in story.variations %}

{{ variation.child_name }}:

{% with step = variation.steps[0] %}{% include "step.jinja2" %}{% endwith %}
{% endfor %}
{% endfor %}

## Install

```sh
$ pip install strictyamljsonschema
```
