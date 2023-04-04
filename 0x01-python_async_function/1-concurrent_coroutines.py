#!/usr/bin/python3
"""execute multiple coroutines at the same time"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int):
    """takes two int arguments n : max_delay, wait_random
        returns a list of all delay(float values)
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
