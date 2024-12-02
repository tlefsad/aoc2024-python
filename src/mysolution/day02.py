#!/usr/bin/env python3
"""Solution to Day 2: Red-Nosed Reports
https://adventofcode.com/2024/day/2
"""
from __future__ import annotations

import dataclasses
import operator
from functools import cached_property
from itertools import combinations, pairwise, starmap
from typing import TextIO, Self, List

from helpers.cli import command_with_input_file, open_input_file


@command_with_input_file
def program(input_file: str) -> None:
    """Main program.
    """
    with open_input_file(input_file) as fobj:
        unusual_data = read_input(fobj)

    # Part 1: How many reports are safe?
    print("Part 1:", unusual_data.safe_reports)

    # Part 2: How many reports are now safe?
    print("Part 2:", unusual_data.more_safe_reports)


def read_input(fobj: TextIO) -> UnusualData:
    """Reads and parses input file according to problem statement.
    """
    return UnusualData.from_str(fobj.readlines())


def satisfy_constraints(nums):
    return all(0 < num <= 3 for num in nums)


def predicate(report):
    nums = list(starmap(operator.sub, pairwise(report)))
    return any(map(satisfy_constraints, (nums, map(operator.neg, nums))))


def predicate_all_combs(report):
    return any(map(predicate, combinations(report, len(report) - 1)))


@dataclasses.dataclass(frozen=True)
class UnusualData:
    reports: List[List[int]]

    @classmethod
    def from_str(cls, lines: List[str]) -> Self:
        return cls(reports=[list(map(int, line.strip().split())) for line in lines])

    @cached_property
    def safe_reports(self) -> int:
        return sum(map(predicate, self.reports))

    @cached_property
    def more_safe_reports(self) -> int:
        return sum(map(predicate_all_combs, self.reports))


if __name__ == '__main__':
    program()
