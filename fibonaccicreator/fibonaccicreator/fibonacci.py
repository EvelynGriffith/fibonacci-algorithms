"""Compute values in the Fibonacci sequence using different approaches."""

# Import all of the needed type annotations
from pyinstrument import Profiler  # type: ignore

import typer

from rich.console import Console

import os
import psutil  # type: ignore
import time

from resource import getrusage, RUSAGE_SELF

from fibonaccicreator import fibonacci


def fibonacci_recursivelist(number: int) -> List[int]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # Base case: return [0, 1] when number is either 0 or 1
    if number == 0 or number == 1:
        return 1
    else: 
    # Recursive case: perform the computation for number - 1 and
    # then append to the list the two previous computations added together
        return fibonacci_recursivelist(number - 1) + fibonacci_recursivelist(number - 2)
    # Finally, return the current version of the list.


def fibonacci_recursivetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # Note that the reference describes the computation for lists and not tuples
    # TODO: Base case: return [0, 1] when number is either 0 or 1
    # TODO: Recursive case: perform the computation for number - 1 and
    # then "append" to the tuple the two previous computations added together,
    # bearing in mind that the use of += will create a new tuple.
    # TODO: Finally, return the current version of the tuple.


def fibonacci_iterativetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using iteration and a tuple."""
    # create an empty tuple that will ultimately contain the results
    result = ()
    # set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    a = 1
    b = 1
    # iterate from zero to the (number)th number
    for i in range(number):
    # --> store the value of a in the tuple
        result += (a,)
    # --> move to the next value such that:
    # --> a gets the current value of b
    # --> b gets the current value of a + b
        a, b = b, a + b
    # return the final tuple that contains the fibonacci numbers
    return result


def fibonacci_iterativelist(number: int) -> List[int]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using a list."""
    # create an empty list that will ultimately contain the results
    result = []
    # set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    a = 1
    b = 1
    # iterate from zero to the (number)th number
    for i in range(number):
    # --> store the value of a in the list
        result.append(a)
    # --> move to the next value such that:
    # --> a gets the current value of b
    # --> b gets the current value of a + b
        a, b = b, a + b
    # return the final tuple that contains the fibonacci numbers
    return result
