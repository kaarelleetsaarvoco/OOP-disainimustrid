from typing import List

class Splitter:
    """
    Splits a square matrix into its rows, columns, and diagonals.
    """
    def split(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Extracts all rows, columns, main diagonal, and anti-diagonal from the matrix.
        
        Args:
            matrix (List[List[int]]): A square 2D list representing the matrix.
        
        Returns:
            List[List[int]]: A list containing all rows, columns, main diagonal, and anti-diagonal.
        """
        n = len(matrix)
        rows = matrix[:]
        cols = [[matrix[i][j] for i in range(n)] for j in range(n)]
        main_diag = [matrix[i][i] for i in range(n)]
        anti_diag = [matrix[i][n - 1 - i] for i in range(n)]
        return rows + cols + [main_diag] + [anti_diag]
