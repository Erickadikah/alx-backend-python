#!/usr/bin/env python3
"""function async genarator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops ten times each time asynchronously waits 1second
        then yeilds a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
