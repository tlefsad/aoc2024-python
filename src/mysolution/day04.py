#!/usr/bin/env python3
"""Solution to Day 4: Ceres Search
https://adventofcode.com/2024/day/4
"""
from __future__ import annotations

import dataclasses
from itertools import starmap
from functools import cached_property
from typing import TextIO, Self, List
from more_itertools import distinct_permutations, iequals

from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        puzzle = read_input(fobj)

    # Part 1: How many times does XMAS appear?
    print("Part 1:", puzzle.p1)

    # Part 2: How many times does an X-MAS appear?
    print("Part 2:", puzzle.p2)


def read_input(fobj: TextIO) -> Puzzle:
    """Reads and parses input file according to problem statement.
    """
    return Puzzle.from_str(fobj.readlines())


@dataclasses.dataclass(frozen=True)
class Puzzle:
    words: List[List[str]]

    @classmethod
    def from_str(cls, lines: List[str]) -> Self:
        rows, cols = len(lines), len(lines[0].strip())
        words = [['']*(cols+6) for _ in range(rows+6)]
        for row, line in enumerate(lines):
            for col, ch in enumerate(line.strip()):
                words[row+3][col+3] = ch
        return cls(words=words)

    @cached_property
    def p1(self) -> int:
        rows, cols, words = len(self.words), len(self.words[0]), self.words
        directions = [tuple(zip(*d)) for d in distinct_permutations(
            [(0, 0, 0), (1, 2, 3), (1, 2, 3), (-1, -2, -3), (-1, -2, -3)], 2)]
        return sum(
            sum(iequals('MAS', (words[r + dr][c + dc] for dr, dc in d)) for d in directions)
            for r in range(rows) for c in range(cols) if words[r][c] == 'X'
        )

    @cached_property
    def p2(self) -> int:
        rows, cols, words = len(self.words), len(self.words[0]), self.words
        directions = [tuple(zip(*d)) for d in distinct_permutations([(1, 0, -1), (-1, 0, 1), (1, 0, -1), (-1, 0, 1)], 2)]
        return sum(
            sum(iequals('MAS', (words[r + dr][c + dc] for dr, dc in d)) for d in directions) == 2
            for r in range(rows) for c in range(cols) if words[r][c] == 'A'
        )


if __name__ == '__main__':
    program()
