#!/usr/bin/env python3
"""first define a variable
"""
from typing import Any, TypeVar, Mapping, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =None) -> Union[Any, T]:
    """ T = defining a type variable
        to specify the variable.
        T = union of type and any
    """
    if key in dct:
        return dct[key]
    else:
        return default
