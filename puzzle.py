#!/usr/bin/python2.7
""" Puzzle Class """

from itertools import chain

class Puzzle:
    """ A class to represent a puzzle. """

    def __init__(self, puzzle):
        """ Initialization.  Requires 2d array as input. """
        self.puzzle = puzzle

    def row(self, row):
        """ Return a row given its index. """
        return self.puzzle[row]

    def col(self, col):
        """ Return a column given its index. """
        return [x[col] for x in self.puzzle]

    def box(self, row, col):
        """ Return a box given its row and column. """
        row_offset = int(len(self.puzzle) / 3)
        col_offset = int(len(self.puzzle[0]) / 3)
        row_start = row * row_offset
        col_start = col * col_offset
        bunch = [x[col_start : col_start + col_offset]
                 for x in self.puzzle[row_start : row_start + row_offset]]
        return list(chain.from_iterable(bunch))
