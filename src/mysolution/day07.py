#!/usr/bin/env python3
"""Solution to Day 7: Bridge Repair
https://adventofcode.com/2024/day/7
"""
from __future__ import annotations

import dataclasses
from functools import cached_property, reduce
from typing import TextIO, Self, List
from operator import add, mul
from itertools import product

from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        puzzle = read_input(fobj)

    # Part 1:
    print("Part 1:", puzzle.p1)

    # Part 2:
    print("Part 2:", puzzle.p2)


def read_input(fobj: TextIO) -> Puzzle:
    """Reads and parses input file according to problem statement.
    """
    return Puzzle.from_str(fobj.readlines())


def evaluate(equations, operators):
    return sum(
        test_value for test_value, numbers in equations
        if any(reduce(lambda x, y: next(func)(x, y), numbers) == test_value
               for func in map(iter, product(operators, repeat=len(numbers) - 1)))
    )


@dataclasses.dataclass(frozen=True)
class Puzzle:
    equations: List[tuple]

    @classmethod
    def from_str(cls, lines: List[str]) -> Self:
        equations = []
        for line in lines:
            test_value, numbers = line.strip().split(':')
            equations.append((int(test_value), tuple(map(int, numbers.strip().split()))))
        return cls(equations=equations)

    @cached_property
    def p1(self) -> int:
        operators = [add, mul]
        return evaluate(self.equations, operators)

    @cached_property
    def p2(self) -> int:
        def concat(x, y):
            return int(str(x) + str(y))
        operators = [add, mul, concat]
        return evaluate(self.equations, operators)


if __name__ == '__main__':
    program()
