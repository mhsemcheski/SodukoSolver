#!/usr/bin/python3
''' soduko solver '''

import copy
from puzzle import Puzzle
from hints import HintGenerator
from stats import PuzzleStats

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

    HINT = HintGenerator(SODUKO)
    HINT.create_hints()
    print(HINT.hint_matrix.box(0, 0))

    STATS = PuzzleStats()
    STATS.set_puzzle(HINT.hint_matrix)
    print(STATS)
