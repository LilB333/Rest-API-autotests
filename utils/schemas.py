get_all_objects = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "pattern": "^\\d+$"
      },
      "name": {
        "type": "string",
        "minLength": 1
      },
      "data": {
        "type": ["object", "null"],
        "additionalProperties": {
          "type": ["string", "number", "null"]
        }
      }
    },
    "required": ["id", "name", "data"],
    "additionalProperties": False
  }
}

post_object = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "name", "data", "createdAt"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-f0-9]+$"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": ["object", "null"],
      "additionalProperties": {
        "type": ["string", "number", "null"]
      }
    },
    "createdAt": {
      "type": "string",
      "format": "date-time"
    }
  },
  "additionalProperties": False
}
