#!/usr/bin/env python3
"""Annotation Function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return Annotation"""
    return [(i, len(i)) for i in lst]
