#!/usr/bin/env python3
"""this function takes in interger as an argument
    returns asyncio.Task
"""
import asyncio
import time



wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """ it takes max_delay as an argument and returns
        asyncio.task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
