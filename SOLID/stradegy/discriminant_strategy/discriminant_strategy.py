from abc import ABC, abstractmethod

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
