import random
from typing import List

class Generator:
    """
    Generates random numbers for creating magic squares.
    """
    def generate(self, length: int) -> List[int]:
        """
        Generates a list of random integers from 1 to 9 of the given length.
        
        Args:
            length (int): The number of random numbers to generate.
        
        Returns:
            List[int]: A list of random integers.
        """
        return [random.randint(1, 9) for _ in range(length)]

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

class Verifier:
    """
    Verifies if all given lists have equal sums.
    """
    def verify(self, lists: List[List[int]]) -> bool:
        """
        Checks if the sum of each list in the input is the same.
        
        Args:
            lists (List[List[int]]): A list of lists to check.
        
        Returns:
            bool: True if all sums are equal, False otherwise.
        """
        if not lists:
            return True
        sums = [sum(lst) for lst in lists]
        return all(s == sums[0] for s in sums)

class MagicSquareGenerator:
    """
    Facade class for generating magic squares using Generator, Splitter, and Verifier.
    """
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size: int) -> List[List[int]]:
        """
        Generates a magic square of the given size.
        
        Args:
            size (int): The size of the square (e.g., 3 for a 3x3 square).
        
        Returns:
            List[List[int]]: A 2D list representing the magic square.
        """
        while True:
            nums = self.generator.generate(size * size)
            matrix = [nums[i * size:(i + 1) * size] for i in range(size)]
            parts = self.splitter.split(matrix)
            if self.verifier.verify(parts):
                return matrix