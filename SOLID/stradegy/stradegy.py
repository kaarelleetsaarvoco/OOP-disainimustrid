import cmath
from abc import ABC, abstractmethod
from typing import Tuple

class DiscriminantStrategy(ABC):
    """
    Abstract base class defining the interface for discriminant calculation strategies.
    
    The discriminant is the value b² - 4ac in the quadratic formula.
    Different strategies may handle this calculation differently,
    particularly for negative discriminants.
    """
    
    @abstractmethod
    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        """
        Calculate the discriminant of a quadratic equation.
        
        Args:
            a (float): Coefficient of x²
            b (float): Coefficient of x
            c (float): Constant term
        
        Returns:
            float: The calculated discriminant (b² - 4ac)
        """
        pass

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
