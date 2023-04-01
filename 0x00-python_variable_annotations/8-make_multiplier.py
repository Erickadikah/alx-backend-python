#!/usr/bin/env python3
"""Function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function"""
    def inner(multiplier: float) -> float:
        """Returns multiplier"""
        return (multiplier * multiplier)
    return inner
