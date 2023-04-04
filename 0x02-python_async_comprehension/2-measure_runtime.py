#!/usr/bin/env python3
"""Couroutine executes async_comprehension
    fourTimes
"""
import asyncio
import time
from  typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """Executing four times in parallel
        using asyncio.gather and measures the time of execution
        and returns the total execution time
    """
    start_time = time.perf_counter()
    my_list = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*my_list)
    total_time = time.perf_counter() - start_time
    return total_time
