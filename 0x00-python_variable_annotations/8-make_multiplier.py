#!/usr/bin/python3
'''Task 8 mod
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Create a multiple function
    '''
    return lambda x: x * multiplier
