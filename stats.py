#!/usr/bin/python3

''' For getting stats about puzzles. '''

from puzzle import Puzzle


class PuzzleStats:

    ''' Class for grabbing stats about puzzles. '''

    def __init__(self):
        """ Initialize. """
        self.puzzle = Puzzle()
        self.stats = {}

    def set_puzzle(self, puzzle):
        """ Set the puzzle. """
        self.puzzle = puzzle
        self.get_count()

    def get_count(self):
        """ Get the count as a dict. """

        for cell in self.puzzle.cells():
            if isinstance(cell.value, list):
                for val in cell.value:
                    self.stats[val] = self.stats.get(val, 0) + 1
            if isinstance(cell.value, int):
                self.stats[cell.value] = self.stats.get(cell.value, 0) + 1


    def __str__(self):
        """ Write out the stats as a string. """

        output = ""
        for k in self.stats:
            output = output + " < {0} : {1} > ".format(k, self.stats[k])

        return output
