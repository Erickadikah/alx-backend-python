#!/usr/bin/env python3
"""a asyncronous coroutine that takes in an interger argument"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """int argument and awaits for random delay and returns delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
