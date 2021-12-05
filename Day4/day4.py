from typing import List, Any, Tuple
from pathlib import Path


def extract_boards(boards_str: List[str]) -> List[Any]:
    boards = []
    for i in range(0, len(boards_str), 6):
        board = []
        for j in range(1, 6):
            board.append([int(value) for value in boards_str[i + j].strip().split()])

        boards.append(board)

    return boards


def read_input(test: bool = False) -> Tuple[List[int], List[Any]]:
    if test:
        with open(f"{Path(__file__).parent}/test_input.txt", "r") as f:
            values = [int(value) for value in f.readline().strip().split(",")]
            boards_str = f.readlines()
            boards = extract_boards(boards_str)

            return values, boards

    with open(f"{Path(__file__).parent}/input.txt", "r") as f:
        values = f.readline().split(",")
        boards_str = f.readlines()
        boards = extract_boards(boards_str)

        return values, boards


def part1(test: bool = False) -> int:
    answer = 0
    values, boards = read_input(test)
    seen_numbers = []
    
    # Could just append first four numbers to seen numbers and start from index four
    # But whaterver, this looks a bit better
    for index, value in enumerate(values):
        if index < 5:
            seen_numbers.append(value)
            continue
        
        for board in boards:
            for row in board:
                if all(value in seen_numbers for value in row):
                    break
        


def part2(test: bool = False) -> Any:
    answer = 0
    values, boards = read_input(test)


