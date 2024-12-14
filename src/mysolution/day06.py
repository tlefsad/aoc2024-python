#!/usr/bin/env python3
"""Solution to Day 6: Guard Gallivant
https://adventofcode.com/2024/day/6
"""
from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TextIO, Self, List
from copy import deepcopy

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
    return Puzzle.from_str(fobj.readlines())


@dataclasses.dataclass(frozen=True)
class Puzzle:
    grid: List[List[str]]

    @classmethod
    def from_str(cls, lines: List[str]) -> Self:
        grid = [list(line.strip()) for line in lines]
        return cls(grid=grid)

    @cached_property
    def p1(self) -> int:
        grid = self.grid
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '^')
        z = 0
        visited = set()
        visited.add((x, y))
        while True:
            dx, dy = directions[z]
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                return len(visited)

            if grid[new_x][new_y] != '#':
                x, y = new_x, new_y
            else:
                z = (z+1) % 4
            visited.add((x, y))

    @cached_property
    def p2(self) -> int:
        grid = self.grid
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0
        start_x, start_y, start_z = next((r, c, 0) for r in range(m) for c in range(n) if grid[r][c] == '^')
        for i in range(m):
            for j in range(n):
                x, y, z = start_x, start_y, start_z
                visited = set()
                while True:
                    if (x, y, z) in visited:
                        ans += 1
                        break
                    visited.add((x, y, z))
                    dx, dy = directions[z]
                    new_x, new_y = x + dx, y + dy
                    if not (0 <= new_x < m and 0 <= new_y < n):
                        break
                    if grid[new_x][new_y] == '#' or (new_x, new_y) == (i, j):
                        z = (z+1) % 4
                    else:
                        x, y = new_x, new_y
        return ans


if __name__ == '__main__':
    program()
