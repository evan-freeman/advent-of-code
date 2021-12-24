def pad_list(list, x_dim):
    """Add a mountain range of value 9 to all sides"""
    for i, row in enumerate(list):
        list[i] = [9] + row + [9]
    list.insert(0, [9] * (x_dim + 2))
    list.append([9] * (x_dim + 2))
    return list


def print_list(list):
    for row in list:
        print(row)


def check_low_point(input, value, i, j):
    up_value = input[i - 1][j]
    down_value = input[i + 1][j]
    left_value = input[i][j - 1]
    right_value = input[i][j + 1]

    up = value < up_value
    down = value < down_value
    left = value < left_value
    right = value < right_value
    return up and down and left and right


def check_all_points(input, x_dim, y_dim):
    output = []
    for i in range(1, y_dim + 1):
        for j in range(1, x_dim + 1):
            value = input[i][j]
            if check_low_point(input, value, i, j):
                output.append(value)
    return output


if __name__ == "__main__":
    filepath = "2021/day9/input.txt"
    with open(filepath) as f:
        input = f.read()
    input = [[int(height) for height in line] for line in input.splitlines()]

    test_input = (
        """2199943210\n3987894921\n9856789892\n8767896789\n9899965678"""
    )
    test_input = [
        [int(height) for height in line] for line in test_input.splitlines()
    ]

    x_dim = len(input[0])
    y_dim = len(input)
    # print_list(test_input)
    # print()
    # print_list(pad_list(test_input, x_dim))

    # padded_test_input = pad_list(test_input, x_dim)
    padded_input = pad_list(input, x_dim)
    output = check_all_points(padded_input, x_dim, y_dim)
    risk_levels = [num + 1 for num in output]
    # print(output)
    # print(risk_levels)
    print(sum(risk_levels))
