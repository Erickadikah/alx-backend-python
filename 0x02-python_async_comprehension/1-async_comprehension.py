#!/usr/bin/env python3
"""Couroutine async_comprehension
    takes no arguments
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehesion
        returns 10 random numbers as values
    """
    random_num = [random_int async for random_int in async_generator()]
    return random_num
