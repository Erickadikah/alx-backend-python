#!/usr/bin/env python3
"""first define a variable
"""
from typing import Dict, TypeVar, Optional


V = TypeVar('V')

def safely_get_value(dct: Dict[str, V], key: str, default: Optional[V] = None) -> Optional[V]:
    """ v = defining a type variable
        to specify the variable.
    """
    if key in dct:
        return dct[key]
    else:
        return default
