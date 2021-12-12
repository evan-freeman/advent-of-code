with open("2021/day4/input.txt") as f:
    input = f.read()
numbers, boards = input.split("\n\n", maxsplit=1)
numbers = [int(x) for x in numbers.split(",")]
boards = boards.split("\n\n")
boards = [board.split("\n") for board in boards]
boards = [[[int(x) for x in row.split()] for row in board] for board in boards]
board_list = []
for board in boards:
    board_list.append(
        {
            "cells": [
                [{"num": num, "marked": 0} for num in row] for row in board
            ],
            "rows": [0, 0, 0, 0, 0],
            "columns": [0, 0, 0, 0, 0],
        }
    )
boards = {
    "board_list": board_list,
    "winning_numbers": [],
    "winning_boards": [],
}


def bingo(numbers, boards):
    # Do rounds of bingo
    while numbers and boards["board_list"]:
        number = numbers.pop(0)
        boards = bingo_round(number, boards)
    return boards["winning_numbers"], boards["winning_boards"]


def bingo_round(number, boards):
    # Mark all boards
    # Remove winning boards
    for board in boards["board_list"]:
        mark_board(number, board)
        if check_board(board):
            boards["winning_numbers"].append(number)
            boards["winning_boards"].append(board)
            boards["board_list"].remove(board)
    return boards


def mark_board(number, board):
    for i, row in enumerate(board["cells"]):
        for j, cell in enumerate(row):
            if cell["num"] == number and not cell["marked"]:
                cell["marked"] = 1
                board["rows"][i] += 1
                board["columns"][j] += 1


def check_board(board, size=5):
    return size in board["rows"] + board["columns"]


def score(number, board):
    unmarked_numbers = [
        cell["num"]
        for row in board["cells"]
        for cell in row
        if not cell["marked"]
    ]
    return sum(unmarked_numbers) * number


winning_numbers, winning_boards = bingo(numbers, boards)

losing_number = winning_numbers[-1]
losing_board = winning_boards[-1]

print(losing_number)
print(losing_board)
print(score(losing_number, losing_board))
