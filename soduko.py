#!/usr/bin/python2.7
''' soduko solver '''

import re
import copy

PUZZLE = """
060003049
030020015
200104000
000300001
910002050
008700920
007040500
000270004
104000700
"""

def generate_matrix(input_puzzle):
    """Generate the matrix from the input"""

    input_puzzle = re.sub("\n", "", input_puzzle)

    puzzle_matrix = []
    for i in range(9):
        puzzle_matrix.append([])
        for j in range(9):
            puzzle_matrix[i].append(j)

    width = 0
    height = 0
    while height < 9:
        while width < 9:
            index = (height * 9) + width
            puzzle_matrix[height][width] = int(input_puzzle[index]) or None
            width = width + 1
        width = 0
        height = height + 1
    return puzzle_matrix


def hint_puzzle(puzzle):
    """ Get the hints """
    hints = copy.deepcopy(puzzle)
    print(hints)

def print_puzzle(puzzle):
    """ Print the puzzle """
    for line in puzzle:
        print(line)


if __name__ == '__main__':
    PUZZLE_MATRIX = generate_matrix(PUZZLE)
    print_puzzle(PUZZLE_MATRIX)
