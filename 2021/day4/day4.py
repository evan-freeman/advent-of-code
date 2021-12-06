from itertools import product

import numpy as np
from numpy.core.fromnumeric import shape

with open("2021/day4/input.txt") as f:
    input = f.read()
# print(input)
numbers, boards = input.split("\n\n", maxsplit=1)
numbers = [int(x) for x in numbers.split(",")]
boards = boards.split("\n\n")
board0 = boards[0]
board0_list = board0.strip("/n").split()
# board0_list = [int(x) for x in board0_list]

combs = list(product(range(5), range(5)))
board0 = np.array(board0_list, dtype=int).reshape(5, 5)
print(board0)


# print(board0_list)
# print(combs)
