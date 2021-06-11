import pathlib
import time
from PIL import Image


def file_exists(file_path, wait_time=10):
    f = pathlib.Path(file_path)
    start_time = time.time()
    while start_time + wait_time >= time.time():
        if f.exists():
            break
    return f.exists()


def file_is_an_image(file_path):
    try:
        Image.open(file_path)
        file_is_image = True
    except IOError:
        file_is_image = False
    return file_is_image
