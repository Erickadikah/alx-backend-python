#!/usr/bin/env python3
""" this function measure time of execution
    for wait_n(n, max_delay) and returns a float.
"""
import asyncio
import time
import random
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """this function takes n and max_delay as argumnets
        measures the total execution time forwait_n(n, max_delay)
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
