from dataclasses import field
from typing import Dict, Any, List

import marshmallow_dataclass
from jsonpath_ng.ext import parse


def get_json_path(json: Dict[str, Any], json_path: str, allow_empty: bool = False) -> List[Any]:
    values = [match.value for match in parse(json_path).find(json)]
    if not allow_empty:
        assert values, f'Parameter: {json_path} is not found'
    return values


@marshmallow_dataclass.dataclass
class BaseModel:

    @classmethod
    def load(cls, response: Dict[str, Any]) -> 'BaseModel':
        return cls.Schema().load(response)

    def dump(self):
        return self.Schema().dump(self)


@marshmallow_dataclass.dataclass()
class AlphabetModel(BaseModel):
    a: str = field(metadata={'data_key': 'a'})
    b: str = field(metadata={'data_key': 'b'})
    c: str = field(metadata={'data_key': 'c'})


response_json = {
    '1': {'a': 'A','b': 'B','c': 'C'},
    '2': {'d': 'D','e': 'E','f': 'F'}
}

response = get_json_path(response_json, json_path='$."1"')[0]

alphabet = AlphabetModel.load(response)
