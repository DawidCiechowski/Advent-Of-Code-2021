from typing import List, Any, Tuple, Optional
from pathlib import Path


def extract_boards(boards_str: List[str]) -> List[Any]:
    boards = []
    for i in range(0, len(boards_str), 6):
        board = []
        for j in range(1, 6):
            board.append(
                [
                    {"value": int(value), "seen": False}
                    for value in boards_str[i + j].strip().split()
                ]
            )

        boards.append(board)

    return boards


def read_input(test: bool = False) -> Tuple[List[int], List[Any]]:
    if test:
        with open(f"{Path(__file__).parent}/test_input.txt", "r") as f:
            values = [int(value) for value in f.readline().strip().split(",")]
            boards = extract_boards(f.readlines())

            return values, boards

    with open(f"{Path(__file__).parent}/input.txt", "r") as f:
        values = [int(value) for value in f.readline().strip().split(",")]
        boards = extract_boards(f.readlines())

        return values, boards


def calculate_total(board: List[List[Any]]) -> int:
    total = 0
    for row in board:
        for position in row:
            if not position["seen"]:
                total += position["value"]

    return total


def check_board(board: List[List[Any]]) -> bool:
    for col_index, row in enumerate(board):
        if all(position["seen"] == True for position in row):
            return True

        if all(board[row_index][col_index]["seen"] == True for row_index in range(5)):
            return True

    return False


def part1(test: bool = False) -> Optional[int]:
    values, boards = read_input(test)

    for value in values:
        for board in boards:
            for row in board:
                for position in row:
                    if value == position["value"]:
                        position["seen"] = True
                if check_board(board):
                    return calculate_total(board) * value

    return None


def part2(test: bool = False) -> Optional[int]:
    values, boards = read_input(test)
    winning_boards = []
    for value in values:
        for board in boards:

            if board in winning_boards:
                continue

            for row in board:
                for position in row:
                    if value == position["value"]:
                        position["seen"] = True
                        break

                if check_board(board):
                    winning_boards.append(board)
                    if len(boards) == len(winning_boards):
                        return calculate_total(winning_boards[len(winning_boards) - 1]) * value
                    else:
                        break
                else:
                    continue
            
    return None

