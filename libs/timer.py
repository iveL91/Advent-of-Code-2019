"""timer"""

import functools
import time
from typing import Callable


def timer(func: Callable) -> Callable:
    """https://realpython.com/python-timer/#creating-a-python-timer-decorator"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time ({func.__name__}): {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer
