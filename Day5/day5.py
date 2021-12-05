from typing import List, Any, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Coordinates:
    x: int
    y: int


@dataclass(frozen=True)
class LineCoordinates:
    starting_coordinates: Coordinates
    end_coordinates: Coordinates


def read_input(test: bool = False) -> Any:
    file_name = "test_input.txt" if test else "input.txt"
    input_values = []
    with open(f"{Path(__file__).parent}/{file_name}", "r") as f:
        for line in f.readlines():
            starting_coordinates, end_coordinates = None, None
            line = line.strip().split("->")
            for index, coordinates in enumerate(line):
                coordinates = coordinates.split(",")
                x, y = int(coordinates[0]), int(coordinates[1])

                if index == 0:
                    starting_coordinates = Coordinates(x, y)
                else:
                    end_coordinates = Coordinates(x, y)
            input_values.append(LineCoordinates(starting_coordinates, end_coordinates))

    return input_values


def part1(test: bool = False) -> Any:
    input_values = read_input(test)
    diagram = {}

    for value in input_values:
        start_x, end_x = value.starting_coordinates.x, value.end_coordinates.x
        start_y, end_y = value.starting_coordinates.y, value.end_coordinates.y
        if (start_x == end_x) and (start_y != end_y):
            starting_y = max(start_y, end_y)
            for i in range(abs(start_y - end_y) + 1):
                intersection = Coordinates(start_x, starting_y - i)

                if intersection in diagram:
                    diagram[intersection] += 1
                else:
                    diagram[intersection] = 1

        if (start_y == end_y) and (start_x != end_x):
            starting_x = max(start_x, end_x)
            for i in range(abs(start_x - end_x) + 1):
                intersection = Coordinates(starting_x - i, start_y)

                if intersection in diagram:
                    diagram[intersection] += 1
                else:
                    diagram[intersection] = 1

    return sum([value > 1 for value in diagram.values()])


def part2(test: bool = False) -> Any:
    input_values = read_input(test)
    diagram = {}

    for value in input_values:
        start_x, end_x = value.starting_coordinates.x, value.end_coordinates.x
        start_y, end_y = value.starting_coordinates.y, value.end_coordinates.y
        if (start_x == end_x) and (start_y != end_y):
            starting_y = max(start_y, end_y)
            for i in range(abs(start_y - end_y) + 1):
                intersection = Coordinates(start_x, starting_y - i)

                if intersection in diagram:
                    diagram[intersection] += 1
                else:
                    diagram[intersection] = 1

        elif (start_y == end_y) and (start_x != end_x):
            starting_x = max(start_x, end_x)
            for i in range(abs(start_x - end_x) + 1):
                intersection = Coordinates(starting_x - i, start_y)

                if intersection in diagram:
                    diagram[intersection] += 1
                else:
                    diagram[intersection] = 1

        else:
            #TODO: Implement the second part of day 5
            pass

    return sum([value > 1 for value in diagram.values()])


print(part1())
