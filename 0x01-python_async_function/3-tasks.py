#!/usr/bin/env python3
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
