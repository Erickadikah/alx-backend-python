#!/usr/bin/env python3
"""annotated function, takes str float or int, returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes str and int or float, returns str, square of v as float"""
    return k, v**2.0
