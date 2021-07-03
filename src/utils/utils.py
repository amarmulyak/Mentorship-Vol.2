"""
Utils module.
"""

import pathlib
import time
from PIL import Image
import pyautogui


def is_file_exists(file_path, wait_time=10):
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


def is_file_an_image(file_path):
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


def move_mouse_to(x, y):
    """
    Move the mouse cursor to specified coordinate.
    E.g. x = 0 and y = 0 is the top right corner.

    :param x: X (Horizontal) coordinate
    :param y: Y (Vertical) coordinate
    :return: None
    """

    pyautogui.moveTo(x, y)
