#!/usr/bin/env python3
""" The types of the elements of the input are not know"""
from typing import List, Union


def safe_first_element(lst: Union[List, str]) -> Union[str, None]:
    if lst:
        return lst[0]
    else:
        """type element is not known"""
        return None
