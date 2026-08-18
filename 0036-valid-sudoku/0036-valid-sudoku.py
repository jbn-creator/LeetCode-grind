class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def colValid(sudoku):
            for rawColumns in zip(*sudoku):
                column =  [x for x in rawColumns if x != "."]
                if len(set(column)) != len(column):
                    return False
            return True
        def subBoxValid(sudoku):
            #didn't know what to write for this one 
        
            for r in range(0, 9, 3):
                for c in range(0, 9, 3):
                    box = [
                        sudoku[r + i][c + j]
                        for i in range(3)
                        for j in range(3)
                        if sudoku[r + i][c + j] != "."
                    ]
                    if len(set(box)) != len(box):
                        return False
            return True
        def rowValid(sudoku):
            for rawRow in sudoku:
                row =  [x for x in rawRow if x != "."]
                if len(set(row)) != len(row):
                    return False
            return True

        
        if colValid(board) and subBoxValid(board) and rowValid(board):
            return True
        return False

    

