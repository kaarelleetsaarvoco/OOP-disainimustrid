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
