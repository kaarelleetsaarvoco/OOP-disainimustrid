from typing import List

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
