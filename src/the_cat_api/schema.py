"""
Module with response schemas

Schema examples:

m_d = {'a': 1, 'b': "hello"}

schema_v = {
    'type': 'object',
    'properties': {'a': {'type': 'number'},
                   'b': {'type': 'string'}}
}

jsonschema.validate(m_d, schema_v)

m_d_2 = [{'a': 1, 'b': "hello"}, {'a': '2', 'b': 'hello2'}]

schema_v_2 = {
    'type': 'array',
    'items': {'type': 'object',
              'properties': {'a': {'type': 'number'},
                             'b': {'type': 'string'}}
              }
    }

jsonschema.validate(m_d_2, schema_v_2)
"""

GET_IMAGES_SCHEMA = {
    'type': 'array',
    'items': {'type': 'object',
              'properties': {'breeds': {'type': 'array'},
                             'id': {'type': 'string'},
                             'url': {'type': 'string'},
                             'weight': {'type': 'number'},
                             'height': {'type': 'number'}}
              }
    }
