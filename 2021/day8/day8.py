import json
import string
from collections import Counter

################################################################################
# Data Prep
################################################################################

letters = list(string.ascii_lowercase[:7])
clock = {
    0: {"segments": ["a", "b", "c", "d", "e", "f"]},
    1: {"segments": ["b", "c"]},
    2: {"segments": ["a", "b", "d", "e", "g"]},
    3: {"segments": ["a", "b", "c", "d", "g"]},
    4: {"segments": ["b", "c", "f", "g"]},
    5: {"segments": ["a", "c", "d", "f", "g"]},
    6: {"segments": ["a", "c", "d", "e", "f", "g"]},
    7: {"segments": ["a", "b", "c"]},
    8: {"segments": ["a", "b", "c", "d", "e", "f", "g"]},
    9: {"segments": ["a", "b", "c", "d", "f", "g"]},
}
for num in clock:
    clock[num]["num_segments"] = len(clock[num]["segments"])

segment_counts = dict(Counter([clock[num]["num_segments"] for num in clock]))
segment_counts_copy = segment_counts.copy()
segment_counts = {
    key: segment_counts_copy[key] for key in sorted(segment_counts_copy)
}
num_segments = {
    count: [num for num in clock if clock[num]["num_segments"] == count]
    for count in segment_counts
}


wires = {
    letter: {
        "numbers": [num for num in clock if letter in clock[num]["segments"]]
    }
    for letter in letters
}
for wire in wires:
    wires[wire]["num_occurances"] = len(wires[wire]["numbers"])

wire_counts = dict(Counter([wires[wire]["num_occurances"] for wire in wires]))
wire_counts_copy = wire_counts.copy()
wire_counts = {key: wire_counts_copy[key] for key in sorted(wire_counts_copy)}
num_wires = {
    count: [wire for wire in wires if wires[wire]["num_occurances"] == count]
    for count in wire_counts
}


# TODO dict of wire occurance counts
# e.g. Only "c" occurs 9 times
# num_occurances = {
#     count: [wire for wire in wires if wires[wire]["num_occurances"] == count]
#     for count in occurance_counts
# }

################################################################################
# Solve
################################################################################


# 1. Find all the representations that are unique


# 2.


# Cycle through each representation, making all possible deductions
# Keep cycling until done.


def process_input(input):
    input_repr, display = [
        [sorted(digit) for digit in digits.split()]
        for digits in input.split("|")
    ]
    return input_repr, display


def solve(input):
    input_repr, display = process_input(input)

    # # Print
    # print("Input_Representations")
    # for i, repr in enumerate(input_repr):
    #     print(i, repr)
    # print()
    # print("Four Digit Display")
    # for i, digit in enumerate(display):
    #     print(i, digit)

    # 1. Determine repr based on number of letters
    digit_reprs = {num: None for num in range(10)}
    for repr in input_repr:
        if len(repr) == 2:
            digit_reprs[1] = repr
        elif len(repr) == 3:
            digit_reprs[7] = repr
        elif len(repr) == 4:
            digit_reprs[4] = repr
        elif len(repr) == 7:
            digit_reprs[8] = repr

    wire_reprs = {}

    wire_repr_counts = dict(
        Counter([wire for digit in input_repr for wire in digit])
    )
    # print(f"{wire_repr_counts=}")

    # Logic
    # a appears in 7 but not 1
    letter_a = list(set(digit_reprs[7]) - set(digit_reprs[1]))[0]
    wire_reprs[letter_a] = "a"
    # e occurs 4 times
    letter_e = [
        letter for letter in wire_repr_counts if wire_repr_counts[letter] == 4
    ][0]
    wire_reprs[letter_e] = "e"
    # f occus 6 times
    letter_f = [
        letter for letter in wire_repr_counts if wire_repr_counts[letter] == 6
    ][0]
    wire_reprs[letter_f] = "f"
    # c occurs 9 times
    letter_c = [
        letter for letter in wire_repr_counts if wire_repr_counts[letter] == 9
    ][0]
    wire_reprs[letter_c] = "c"
    # b occurs 8 times and isn't a
    letter_b = [
        letter for letter in wire_repr_counts if wire_repr_counts[letter] == 8
    ]
    letter_b.remove(letter_a)
    letter_b = letter_b[0]
    wire_reprs[letter_b] = "b"
    # g occurs in 4 and isn't b, c, f
    letter_g = digit_reprs[4]
    letter_g.remove(letter_b)
    letter_g.remove(letter_c)
    letter_g.remove(letter_f)
    letter_g = letter_g[0]
    wire_reprs[letter_g] = "g"
    # d occurs in 8 and isn't any other letter
    letter_d = digit_reprs[8]
    letter_d.remove(letter_a)
    letter_d.remove(letter_b)
    letter_d.remove(letter_c)
    letter_d.remove(letter_e)
    letter_d.remove(letter_f)
    letter_d.remove(letter_g)
    letter_d = letter_d[0]
    wire_reprs[letter_d] = "d"

    # print()
    # print(f"{digit_reprs=}")
    # print()
    # print(f"{wire_reprs=}")

    for i, digit in enumerate(display):
        display[i] = sorted([wire_reprs[wire] for wire in digit])

    translation_key = {
        frozenset(clock[digit]["segments"]): digit for digit in clock
    }
    # print(f"{translation_key=}")

    # Print
    # print()
    # print("Four Digit Display")
    # for i, digit in enumerate(display):
    #     print(i, digit)

    digits = [translation_key[frozenset(digit)] for digit in display]
    num = int("".join([str(x) for x in digits]))

    return num


if __name__ == "__main__":
    num_to_process = 1

    file = "2021/day8/input.txt"
    with open(file) as f:
        inputs = f.read()
    inputs = inputs.splitlines()
    # print(input)
    total = 0
    for input in inputs:
        total += solve(input)
    print(total)

    ############################################################################
    # Print
    ############################################################################

    # print()
    # print("Reference Material")
    # print(f"{segment_counts=}")
    # print(f"{num_segments=}")
    # print(f"{wire_counts=}")
    # print(f"{num_wires=}")

    # print()
    # print("Wires")
    # print(json.dumps(wires, indent=4))

    # print()
    # print("Clock")
    # print(json.dumps(clock, indent=4))

    # input_repr, display = process_input(input)
    # print(input_repr)
    # print(display)

    # print(wires)
    # print([wires[wire]["num_occurances"] for wire in wires])
