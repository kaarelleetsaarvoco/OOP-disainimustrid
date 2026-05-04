from stradegy.discriminant_strategy.discriminant_strategy import DiscriminantStrategy

class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    """
    Strategy that calculates the discriminant normally.
    
    Returns the discriminant value as-is, even if negative.
    This allows for complex number solutions in the quadratic equation solver.
    """
    
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        """
        Calculate the discriminant without any special handling.
        
        Args:
            a (float): Coefficient of x²
            b (float): Coefficient of x
            c (float): Constant term
        
        Returns:
            float: The discriminant value (b² - 4ac), may be negative
        """
        return b * b - 4 * a * c
