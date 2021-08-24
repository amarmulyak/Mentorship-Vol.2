"""
Utils module.
"""

from jsonpath_ng.ext import parse
import pathlib
import time
from typing import Dict, Any, List

import aumbry
import pyautogui
import yaml
from PIL import Image
# from selenium.common.exceptions import ErrorInResponseException
from selenium.common import exceptions

from models.config import Config


def get_json_path(json: Dict[str, Any], json_path: str, allow_empty: bool = False) -> List[Any]:
    values = [match.value for match in parse(json_path).find(json)]
    if not allow_empty:
        assert values, f'Parameter: {json_path} is not found'
    return values


def get_base_path() -> pathlib.PosixPath:
    """
    Get the root folder path of the project.

    :return: PosixPath
    """

    return pathlib.Path(__file__).parent.parent.parent


def cfg() -> Config:
    """
    Get config as an object

    :return: Config object
    """

    cfg_ = aumbry.load(
        aumbry.FILE, Config, {"CONFIG_FILE_PATH": f"{get_base_path()}/cfg/cfg.yaml"}
    )
    return cfg_


def cfg_as_dict() -> Dict:
    """
    Get config as dictionary

    :return: Config dict
    """

    with open(f"{get_base_path()}/cfg/cfg.yaml") as f:
        cfg_ = yaml.load(f)
    return cfg_


def is_file_exists(file_path: str, wait_time: int = 10) -> bool:
    """
    Check if file exists.

    :param file_path: Path to file
    :param wait_time: Time
    :return: True or False
    """

    f_path = pathlib.Path(file_path)
    start_time = time.time()
    while start_time + wait_time >= time.time():
        if f_path.exists():
            return f_path.exists()


def is_file_an_image(file_path: str) -> bool:
    """
    Check if file is an image.

    :param file_path: Path to file
    :return: True or False
    """

    try:
        Image.open(file_path)
        file_is_image = True
    except IOError:
        file_is_image = False
    return file_is_image


def move_mouse_to(x_coor: int, y_coor: int) -> None:
    """
    Move the mouse cursor to specified coordinate.
    E.g. x_coor = 0 and y_coor = 0 is the top right corner.

    :param x_coor: X (Horizontal) coordinate
    :param y_coor: Y (Vertical) coordinate
    :return: None
    """

    pyautogui.moveTo(x_coor, y_coor)


def retry(time_out: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            end_time = time.time() + time_out
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if time.time() > end_time:
                        raise AssertionError(e) from None
                    time.sleep(1)

        return wrapper

    return decorator
