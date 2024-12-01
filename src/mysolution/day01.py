#!/usr/bin/env python3
"""Solution to Day 1: Historian Hysteria
https://adventofcode.com/2024/day/1
"""
from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TextIO, Self, List
from collections import Counter


from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        location_ids = read_input(fobj)

    # Part 1: What is the total distance between your lists?
    print("Part 1:", location_ids.total_distance)

    # Part 2: What is their similarity score?
    print("Part 2:", location_ids.similarity_score)


def read_input(fobj: TextIO) -> LocationIDs:
    """Reads and parses input file according to problem statement.
    """
    return LocationIDs.from_str(fobj.readlines())


@dataclasses.dataclass(frozen=True)
class LocationIDs:
    fst_list: List[int]
    snd_list: List[int]

    @classmethod
    def from_str(cls, lines: List[str]) -> Self:
        return cls(*zip(*(map(int, line.strip().split()) for line in lines)))

    @cached_property
    def total_distance(self) -> int:
        return sum(abs(x - y) for x, y in zip(sorted(self.fst_list), sorted(self.snd_list)))

    @cached_property
    def similarity_score(self) -> int:
        counter = Counter(self.snd_list)
        return sum(num * counter[num] for num in self.fst_list)


if __name__ == '__main__':
    program()
