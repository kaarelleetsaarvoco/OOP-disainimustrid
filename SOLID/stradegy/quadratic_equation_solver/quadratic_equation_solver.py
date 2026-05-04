import cmath
from typing import Tuple
from stradegy.discriminant_strategy.discriminant_strategy import DiscriminantStrategy

class QuadraticEquationSolver:
    """
    Solves quadratic equations using a specified discriminant calculation strategy.
    
    The quadratic formula is: x = (-b ± √discriminant) / (2a)
    The strategy determines how the discriminant is calculated.
    """
    
    def __init__(self, strategy: DiscriminantStrategy):
        """
        Initialize the solver with a discriminant calculation strategy.
        
        Args:
            strategy (DiscriminantStrategy): The strategy to use for discriminant calculation
        """
        self.strategy = strategy
    
    def solve(self, a: float, b: float, c: float) -> Tuple[complex, complex]:
        """
        Solve the quadratic equation ax² + bx + c = 0.
        
        Uses the quadratic formula with the strategy's discriminant calculation.
        
        Args:
            a (float): Coefficient of x²
            b (float): Coefficient of x
            c (float): Constant term
        
        Returns:
            Tuple[complex, complex]: A tuple of two solutions (x₁, x₂)
                where x₁ is the solution with + and x₂ is with -
        """
        # Get the discriminant using the strategy
        discriminant = self.strategy.calculate_discriminant(a, b, c)
        
        # Calculate the square root of the discriminant
        sqrt_discriminant = cmath.sqrt(discriminant)
        
        # Calculate both solutions using the quadratic formula
        x1 = (-b + sqrt_discriminant) / (2 * a)  # Plus solution
        x2 = (-b - sqrt_discriminant) / (2 * a)  # Minus solution
        
        return (x1, x2)
