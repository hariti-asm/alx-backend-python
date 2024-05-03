#!/usr/bin/env python3
'''
    Write a type-annotated function element_length that takes a list of
    strings lst as input and returns a list of tuples of the form (element,
    length)
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples of the form (element, length)
    """
    return [(i, len(i)) for i in lst]
