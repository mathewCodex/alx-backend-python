#!/usr/bin/env python3
'''Task 7 mod
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Con a key and val to a tuple of the key
    '''
    return (k, float(v**2))
