"""config module."""

import aumbry
from aumbry import Attr


class CatAPI(aumbry.YamlConfig):
    """
    A class to represent "the_cat_api" subgroup of the config
    """

    __mapping__ = {
        'url': Attr('url', str),
        'x_api_key': Attr('x_api_key', str),
    }


class Config(aumbry.YamlConfig):
    """A class to map config file with its object
    (i.e. cfg/cfg.yaml).
    """

    __mapping__ = {
        "base_url": Attr("base_url", str),
        "browser": Attr("browser", str),
        "the_cat_api": Attr("the_cat_api", CatAPI),
    }
