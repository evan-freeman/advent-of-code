import re
from itertools import chain


def process_input():
    with open("2021/day5/input.txt") as f:
        input = f.read()

    # input = """0,9 -> 5,9
    # 8,0 -> 0,8
    # 9,4 -> 3,4
    # 2,2 -> 2,1
    # 7,0 -> 7,4
    # 6,4 -> 2,0
    # 0,9 -> 2,9
    # 3,4 -> 1,4
    # 0,0 -> 8,8
    # 5,5 -> 8,2
    # """

    # input = """0,2 -> 2,0
    # """

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
    return lines


def sign(x):
    return (x > 0) - (x < 0)


def generate_points(line):
    # add point to list, take a step, repeat
    x1, x2, y1, y2 = line["x1"], line["x2"], line["y1"], line["y2"]
    points = set()
    x_dir = sign(x2 - x1)
    y_dir = sign(y2 - y1)

    while x1 != x2 or y1 != y2:
        points.add((x1, y1))
        # print((x1, y1))
        # print(points)
        x1 += x_dir
        y1 += y_dir
    # Ugh, hacks
    points.add((x1, y1))
    return points


def form_matrix(lines):
    dim = max(chain(*[line.values() for line in lines])) + 1
    matrix = [[0] * dim for i in range(dim)]
    return matrix


def draw_lines_on_matrix(lines, matrix):
    for line in lines:
        for y, x in generate_points(line):
            matrix[x][y] += 1
    num_points = sum([x for row in matrix for x in row if x > 1])
    num_overlaps = len([x for row in matrix for x in row if x > 1])
    return num_points, num_overlaps


def main():
    lines = process_input()
    matrix = form_matrix(lines)
    num_points, num_overlaps = draw_lines_on_matrix(lines, matrix)
    # for row in matrix:
    #     print(row)
    print(num_points)
    print(num_overlaps)


if __name__ == "__main__":
    main()
