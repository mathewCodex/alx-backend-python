#!/usr/bin/env python3
'''Task 1 mod
'''
from typing import List
from importlib import import_module as string


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Create a list of 10 numb from a 10-numb gen
    '''
    return [num async for num in async_generator()]
