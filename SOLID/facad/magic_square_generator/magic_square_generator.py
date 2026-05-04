from typing import List
from facad.generator.generator import Generator
from facad.splitter.splitter import Splitter
from facad.verifier.verifier import Verifier

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
