#!/usr/bin/env python3
"""Solution to Day 5: Print Queue
https://adventofcode.com/2024/day/5
"""
from __future__ import annotations

import dataclasses
from functools import cached_property, cmp_to_key
from typing import Callable, TextIO, Self, List
from more_itertools import is_sorted

from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        puzzle = read_input(fobj)

    # Part 1: What do you get if you add up the middle page number from those correctly-ordered updates?
    print("Part 1:", puzzle.p1)

    # Part 2:
    print("Part 2:", puzzle.p2)


def read_input(fobj: TextIO) -> Puzzle:
    """Reads and parses input file according to problem statement.
    """
    return Puzzle.from_str(fobj.read())


@dataclasses.dataclass(frozen=True)
class Puzzle:
    rules: set[tuple]
    pages: List[list]

    @classmethod
    def from_str(cls, lines: str) -> Self:
        fst_section, snd_section = lines.split('\n\n')
        rules = set(tuple(map(int, line.strip().split('|'))) for line in fst_section.split('\n'))
        pages = [list(map(int, line.strip().split(','))) for line in snd_section.split('\n')]
        return cls(rules=rules, pages=pages)

    @cached_property
    def ordering(self) -> Callable:
        def priority(prev_page, curr_page) -> int:
            return -1 if (prev_page, curr_page) in self.rules else 0
        return cmp_to_key(priority)

    @cached_property
    def p1(self) -> int:
        return sum(page[len(page)//2] for page in self.pages if is_sorted(page, key=self.ordering))

    @cached_property
    def p2(self) -> int:
        return sum(
            sorted_page[len(sorted_page)//2]
            for page in self.pages
            if (sorted_page := sorted(page, key=self.ordering)) != page
        )


if __name__ == '__main__':
    program()
