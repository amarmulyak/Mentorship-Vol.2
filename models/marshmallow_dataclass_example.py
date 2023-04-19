from typing import Dict, Any

from dataclasses import field
import marshmallow_dataclass


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


response = {
    'a': 'A',
    'b': 'B',
    'c': 'C'
}

alphabet = AlphabetModel.load(response)
