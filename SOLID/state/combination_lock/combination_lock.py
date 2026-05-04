from typing import List

class CombinationLock:
    """
    A combination lock that changes its state based on the digits entered by the user.
    
    The lock has three main states:
    - 'LOCKED': Initial state
    - A string of entered digits (e.g., '123'): While entering the combination
    - 'OPEN': When the correct combination is entered
    - 'ERROR': When an incorrect digit is entered that doesn't match the expected combination
    """
    
    def __init__(self, combination: List[int]):
        """
        Initialize the combination lock with the correct combination.
        
        Args:
            combination (List[int]): The correct combination sequence of digits.
        """
        self.combination = combination
        self.status: str = 'LOCKED'
        self.entered: List[int] = []
    
    def enter_digit(self, digit: int) -> None:
        """
        Enter a single digit into the lock.
        
        The status is updated based on the entered digits:
        - If digits match the beginning of the correct combination, status shows the digits
        - If all digits are entered correctly, status becomes 'OPEN'
        - If a digit doesn't match the expected position, status becomes 'ERROR'
        
        Args:
            digit (int): The digit to enter.
        """
        self.entered.append(digit)
        
        # Check if the entered digits match the beginning of the combination
        if self._is_correct_so_far():
            # If all digits are entered and correct
            if len(self.entered) == len(self.combination):
                self.status = 'OPEN'
            else:
                # Show the entered digits as a string
                self.status = ''.join(map(str, self.entered))
        else:
            # If the entered digits don't match the combination
            self.status = 'ERROR'
    
    def _is_correct_so_far(self) -> bool:
        """
        Check if the entered digits so far match the beginning of the correct combination.
        
        Returns:
            bool: True if entered digits match the expected prefix, False otherwise.
        """
        if len(self.entered) > len(self.combination):
            return False
        
        for i in range(len(self.entered)):
            if self.entered[i] != self.combination[i]:
                return False
        
        return True
