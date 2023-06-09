#!/usr/bin/python3
"""
    module type anotation function zoom_array
    takes list of type List
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List[int]:
    """
    return: zoomed_in: List
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
