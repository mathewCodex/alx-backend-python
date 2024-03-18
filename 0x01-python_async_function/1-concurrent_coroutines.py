#!/usr/bin/env python3
'''Task 1 mod
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Exec wait_random n times
    '''
    wait_time = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
            )
    return sorted(wait_times)
