#!/usr/bin/python3
''' Hint Generator '''


from puzzle import Puzzle


class HintGenerator:
    """ Hint Generator """

    def __init__(self, input_puzzle):
        """ Initialization """

        self.puzzle = input_puzzle
        self.hint_matrix = Puzzle(len(self.puzzle.rows()), len(self.puzzle.cols()))

    def set_puzzle(self, input_puzzle):
        """ Set the puzzle to use. """
        self.puzzle = input_puzzle

    def create_hints(self):
        """ Do the hints. """

        default_hint = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for cell in self.puzzle.cells():
            if cell.value < 1:
                row = self.puzzle.row(cell.row)
                col = self.puzzle.col(cell.col)
                box = self.puzzle.box(cell.box_x, cell.box_y)
                hint = cell.prune(default_hint, [row, col, box])
                self.hint_matrix.set_cell(cell.row, cell.col, hint)

def test_hints():
    """ Test Hints """

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
    hint = HintGenerator(puzz)
    hint.create_hints()
    print(hint.hint_matrix)


if __name__ == "__main__":
    test_hints()
