#!/usr/bin/env python3
"""Couroutine async_comprehension
    takes no arguments
"""
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Collects 10 random numbers using an async comprehesion
        returns 10 random numbers
    """
    random_num = [list_int async for list_int in async_generator()]
    return random_num
