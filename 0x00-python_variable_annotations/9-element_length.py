#!/usr/bin/python3
"""Anotation Function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotation"""
    return [(i, len(i)) for i in lst]
