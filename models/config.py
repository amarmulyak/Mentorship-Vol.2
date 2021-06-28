"""config module."""

import aumbry
from aumbry import Attr


class Config(aumbry.YamlConfig):
    """A class to map config file with its object
    (i.e. cfg/cfg.yaml).
    """

    __mapping__ = {
        "base_url": Attr("base_url", str),
        "browser": Attr("browser", str),
    }
