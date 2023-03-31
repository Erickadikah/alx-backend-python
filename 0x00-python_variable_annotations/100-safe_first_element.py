#!/usr/bin/env python3
""" The types of the elements of the input are not know"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """args of lst: Sequence[Any]
        return value: 0 or None
    """
    if lst:
        return lst[0]
    else:
        """type element is not known"""
        return None
