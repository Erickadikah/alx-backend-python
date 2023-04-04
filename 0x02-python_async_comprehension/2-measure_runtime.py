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
    my_list = []
    start_time = time.perf_counter()
    for i in range(4):
        task = asyncio.create_task(async_comprehension())
        my_list.append(task)
    result = await asyncio.gather(*my_list)
    total_time = time.perf_counter() - start_time
    return total_time
