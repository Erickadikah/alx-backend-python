#!/usr/bin/env python3
import asyncio
from typing import List
from asyncio.tasks import Task


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """takes two int arguments n : max_delay, wait_random
        returns a list of all delay(float values)
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
