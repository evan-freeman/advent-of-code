import re
from itertools import chain

with open("2021/day5/input.txt") as f:
    input = f.read()

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

input = """0,9 -> 5,9
8,0 -> 0,8
"""

input = [input.split("\n")][0]
del input[-1]
lines = []
regex = ",| -> "
for line in input:
    split_line = re.split(regex, line)
    lines.append(
        {
            "x1": int(split_line[0]),
            "y1": int(split_line[1]),
            "x2": int(split_line[2]),
            "y2": int(split_line[3]),
        }
    )


def generate_points(line):
    x1 = min(line["x1"], line["x2"])
    x2 = max(line["x1"], line["x2"])
    y1 = min(line["y1"], line["y2"])
    y2 = max(line["y1"], line["y2"])
    if x1 == x2:
        return [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(x1, x2 + 1)]
    else:
        # Generate set of diagonal points
        points = []
        while x1 <= x2 or y1 <= y2:
            points.append((x1, y1))
            x1 += 1
            y1 += 1
        return points


dim = max(chain(*[line.values() for line in lines])) + 1
matrix = [[0] * dim for i in range(dim)]

for line in lines:
    # print(line)
    for points in generate_points(line):
        # print(points)
        matrix[points[1]][points[0]] += 1
num_points = sum([x for row in matrix for x in row if x > 1])
num_overlaps = len([x for row in matrix for x in row if x > 1])

for row in matrix:
    print(row)
print(num_points)
print(num_overlaps)
