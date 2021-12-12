from typing import List, Any
from pathlib import Path

def read_input(test: bool = False) -> List[Any]:
    file_name = "test_input.txt" if test else "input.txt"
    with open(f"{Path(__file__).parent}/{file_name}", "r") as f:
        return [int(num) for num in f.read().split(",")]
    
    
def part1(test=False):
    input = read_input(test)
    for _ in range(80):
        newborns = []
        for index in range(len(input)):
            input[index] -= 1
            if input[index] < 0:
                input[index] = 6
                newborns.append(8)
                
        input.extend(newborns)
        
    print(len(input))

def part2(test = False):
    pass

part1(True)