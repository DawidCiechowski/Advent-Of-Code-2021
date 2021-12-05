from  typing import List
from pathlib import Path

def read_input(test: bool = False) -> List[str]:
    if test:
        with open(f"{Path(__file__).parent}/test_input.txt", "r") as f:
            return [value.split(" ") for value in f.readlines()]
        
    with open(f"{Path(__file__).parent}/input.txt", "r") as f:
        return [value.split(" ") for value in f.readlines()]

        
def part1(test: bool = False) -> int:
    input_values = read_input(test)
    position = {"depth": 0, "horizontal": 0}
    
    for direction, distance in input_values:
        if direction == "forward":
            position["horizontal"] += int(distance)
        elif direction == "down":
            position["depth"] += int(distance)     
        else:
            position["depth"] -= int(distance)
            
    return position["depth"] * position["horizontal"]

def part2(test: bool = False) -> int:
    input_values = read_input(test)
    position = {"depth": 0, "horizontal": 0, "aim": 0}

    for direction, distance in input_values:
        if direction == "forward":
            position["horizontal"] += int(distance)
            position["depth"] += position["aim"] *  int(distance)
        elif direction == "down":
            position["aim"] += int(distance)     
        else:
            position["aim"] -= int(distance)
        
    return position["depth"] * position["horizontal"]

