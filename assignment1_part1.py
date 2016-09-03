#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 Assignment 1"""


def listDivide(numbers, divide=2):
    """A func that returns the number of int
    that are div by another number.

    Args:
        numbers (list): A list if int
        divide (int, default = 2): A divisor

    Returns:
        listlen (int): Length of list (numbers that are div by divide).
    Example:
        listDivide([2, 4, 6, 8, 10])
        >>> 5
    """
    divisible = []
    for number in numbers:
        if (int(number) % int(divide)) == 0:
            divisible.append(number)
    listlen = len(divisible)
    return listlen


class ListDivideException(Exception):
    """Exception class"""
    pass


def testListDivide():
    """a test for the listDivide function."""

    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Caught!")
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Caught!")
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Caught!")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Caught!")
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Caught!")


testListDivide()
