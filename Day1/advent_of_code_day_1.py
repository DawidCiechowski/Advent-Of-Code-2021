from typing import List
from pathlib import Path

def get_input_values(test: bool = False) -> List[int]:
    file_name = "test_input.txt" if test else "input.txt"

    with open(f"{Path(__file__).parent}/{file_name}") as f:
        return [int(value) for value in f.readlines()]
    
    
def part1(test: bool = False):
    answer = 0
    input_values = get_input_values(test)

    for index, value in enumerate(input_values):
        if index == 0:
            continue

        if value > input_values[index - 1]:
            answer += 1

    return answer

def part2(test: bool = False):
    answer = 0
    input_values = get_input_values(test)
    
    for i in range(2, len(input_values) - 1):
        previous_sum = input_values[i-2] + input_values[i-1] + input_values[i]
        current_sum = input_values[i-1] + input_values[i] + input_values[i+1]
        
        if current_sum > previous_sum:
            answer += 1
            
    return answer
