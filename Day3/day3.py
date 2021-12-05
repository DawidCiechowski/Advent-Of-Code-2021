from typing import List, Any
from pathlib import Path

def read_input(test: bool = False) -> List[Any]:
    if test:
        with open(f"{Path(__file__).parent}/test_input.txt", "r") as f:
            return [value for value in f.readlines()]
    
    with open(f"{Path(__file__).parent}/input.txt", "r") as f:
            return [value for value in f.readlines()]
        
        
def part1(test: bool = False) -> Any:
    pass

def part2(test:bool = False) -> Any:
    pass