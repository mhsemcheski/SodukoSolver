#!/usr/bin/python2.7

""" Puzzle Class """

from itertools import chain
import re

class Cell:
    """ A class which represents a single cell in a puzzle. """

    def __init__(self, x, y, box_x, box_y, value):
        self.row = x
        self.col = y
        self.box_x = box_x
        self.box_y = box_y
        self.value = 0
        try:
            self.value = int(value)
        except ValueError:
            pass

    def prune(self, candidate, info):
        """ Utility to prune the duplicates from other rows out of a candidate hint list. """

        scand = set(candidate)
        sinfo = set(chain.from_iterable(info))
        return list(scand.difference(sinfo))

    def __str__(self):
        return "[x: {0}, y: {1}, box_x: {2}, box_y: {3}, cell: {4}]".format(self.row, self.col, self.box_x, self.box_y, self.value)

class Puzzle:

    """ A class to represent a puzzle. """

    BOX_SIZE = 3

    def __init__(self, row_count=9, col_count=9):
        """ Initialization.  Requires 2d array as input. """

        self.puzzle = list()
        for rows in range(row_count):
            self.puzzle.append([])
            for _ in range(col_count):
                self.puzzle[rows].append(None)

    def cells(self):
        """ Get a list of cells. """
        row_size = len(self.rows())
        col_size = len(self.cols())

        for row1 in range(row_size):
            for col1 in range(col_size):
                yield Cell(row1, col1,
                           int(row1 / self.BOX_SIZE), int(col1 / self.BOX_SIZE),
                           self.puzzle[row1][col1])

    def set_cell(self, row_index, col_index, value):
        """ Set the value of a cell. """

        self.puzzle[row_index][col_index] = value

    def rows(self):
        '''Collection of rows'''
        return [x for x in self.puzzle]

    def row(self, row_index):
        """ Return a row given its index. """
        return self.puzzle[row_index]

    def cols(self):
        '''Collection of columns'''
        columns = []
        for column_index in range(len(self.rows())):
            columns.append(self.col(column_index))
        return columns

    def col(self, col_index):
        """ Return a column given its index. """
        return [x[col_index] for x in self.puzzle]

    def box_x_max(self):
        """ Return the number of boxes across """
        return int(len(self.rows())/ Puzzle.BOX_SIZE)

    def box_y_max(self):
        """ Return the number of boxes up and down """
        return int(len(self.cols())/ Puzzle.BOX_SIZE)

    def boxes(self):
        """ Return a list of boxes """
        boxes = []

        for horiz in range(self.box_x_max()):
            for vert in range(self.box_y_max()):
                boxes.append(self.box(horiz, vert))
        return boxes

    def box(self, row_index, col_index):
        """ Return a box given its row and column. """
        row_offset = int(len(self.rows()) / self.box_x_max())
        col_offset = int(len(self.cols()) / self.box_y_max())
        row_start = row_index * row_offset
        col_start = col_index * col_offset
        bunch = [x[col_start : col_start + col_offset]
                 for x in self.puzzle[row_start : row_start + row_offset]]
        return list(chain.from_iterable(bunch))


    def from_string(self, input_puzzle):
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

                char = 0
                try:
                    char = int(input_puzzle[index])
                except ValueError:
                    pass
                puzzle_matrix[height][width] = char

                width = width + 1
            width = 0
            height = height + 1

        self.puzzle = puzzle_matrix

    def __str__(self):
        row_separator = " --- --- --- \n"
        cell_separator = "|"
        output = row_separator

        cols = 0
        rows = 0
        for row1 in self.rows():
            output = output + cell_separator
            for char in row1:
                output = output + char.__str__()
                cols = cols + 1

                if cols % Puzzle.BOX_SIZE == 0:
                    output = output + cell_separator

            output = output + "\n"
            rows = rows + 1
            if rows % Puzzle.BOX_SIZE == 0:
                output = output + row_separator

        return output


def test_puzzle():
    """ Run some tests."""
    puzz = Puzzle()

    puzz.from_string("""
7  196 53
   28    
9 14     
 976 8312
61     84
5823 197 
     72 5
    34   
14 562  7
""")

    print(puzz)
    for box in puzz.boxes():
        print(box)

    for row in puzz.rows():
        print(row)

    for col in puzz.cols():
        print(col)

    for cell in puzz.cells():
        print(cell)

if __name__ == "__main__":
    test_puzzle()
