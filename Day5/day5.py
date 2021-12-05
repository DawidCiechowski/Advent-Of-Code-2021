from typing import List, Any, Tuple, Optional
from pathlib import Path


def read_input(test: bool = False) -> Any:

    file_name = "test_input.txt" if test else "input.txt"

    with open(f"{Path(__file__).parent}/{file_name}", "r") as f:
        pass


def part1(test: bool = False) -> Any:
    diagram = [[{"x": x, "y": y} for x in range(9)] for y in range(9)]
    input_values = read_input(test)


def part2(test: bool = False) -> Any:
    input_values = read_input(test)

part1()