from typing import List, Any
from pathlib import Path

def read_input(test: bool = False) -> List[Any]:
    file_name = "test_input.txt" if test else "input.txt"

    with open(f"{Path(__file__).parent}/{file_name}", "r") as f:
            return [value for value in f.readlines()]
        
        
def part1(test: bool = False) -> Any:
    pass

def part2(test:bool = False) -> Any:
    pass