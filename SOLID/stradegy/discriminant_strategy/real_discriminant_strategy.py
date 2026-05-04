from stradegy.discriminant_strategy.discriminant_strategy import DiscriminantStrategy

class RealDiscriminantStrategy(DiscriminantStrategy):
    """
    Strategy that calculates the discriminant with real number constraints.
    
    Returns NaN (not a number) if the discriminant is negative,
    since real numbers cannot be the square root of negative values.
    """
    
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        """
        Calculate the discriminant, returning NaN for negative values.
        
        Args:
            a (float): Coefficient of x²
            b (float): Coefficient of x
            c (float): Constant term
        
        Returns:
            float: The discriminant value, or float('nan') if negative
        """
        discriminant = b * b - 4 * a * c
        
        if discriminant < 0:
            return float('nan')
        
        return discriminant
