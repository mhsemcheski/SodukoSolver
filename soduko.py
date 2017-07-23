#!/usr/bin/python2.7
''' soduko solver '''

import copy
from puzzle import Puzzle
from hints import HintGenerator

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


def hint_puzzle(puzzle):
    """ Get the hints """
    hints = copy.deepcopy(puzzle)
    print(hints)

def print_puzzle(puzzle):
    """ Print the puzzle """
    for line in puzzle:
        print(line)


if __name__ == '__main__':
    SODUKO = Puzzle()
    SODUKO.from_string(PUZZLE)

    print_puzzle(SODUKO.puzzle)
    print(SODUKO)

    hint = HintGenerator(SODUKO)
    hint.create_hints()
    print(hint.hint_matrix.box(0,0))
