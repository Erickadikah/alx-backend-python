#!/usr/bin/env python3
"""function async genarator"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """loops ten times each time asynchronously waits 1second
        then yeilds a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
