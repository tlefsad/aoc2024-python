#!/usr/bin/env python3
"""Solution to Day 3: Mull It Over
https://adventofcode.com/2024/day/3
"""
from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TextIO, Self
import re

from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        memory = read_input(fobj)

    # Part 1: What do you get if you add up all of the results of the multiplications?
    print("Part 1:", memory.multiplications)

    # Part 2: what do you get if you add up all of the results of just the enabled multiplications?
    print("Part 2:", memory.enabled_multiplications)


def read_input(fobj: TextIO) -> Memory:
    """Reads and parses input file according to problem statement.
    """
    return Memory.from_str(fobj.read())


def evaluate(instructions: str) -> int:
    pattern = r'mul\((\d+),(\d+)\)'
    return sum(int(x) * int(y) for x, y in re.findall(pattern, instructions))


@dataclasses.dataclass(frozen=True)
class Memory:
    instructions: str

    @classmethod
    def from_str(cls, lines: str) -> Self:
        return cls(instructions=lines)

    @cached_property
    def multiplications(self) -> int:
        return evaluate(self.instructions)

    @cached_property
    def enabled_multiplications(self) -> int:
        enabled, *disabled = self.instructions.split("don't()")
        return evaluate(enabled) + sum(evaluate(d[d.find("do()"):]) for d in disabled)


if __name__ == '__main__':
    program()
