import aumbry
from aumbry import Attr


class Config(aumbry.YamlConfig):
    __mapping__ = {
        'base_url': Attr('base_url', str),
    }
