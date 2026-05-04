from typing import Union

class Square:
    """
    Represents a square shape with a single side length attribute.
    """
    def __init__(self, side: float = 0):
        """
        Initialize a Square.
        
        Args:
            side (float): The length of the square's side. Defaults to 0.
        """
        self.side = side

def calculate_area(rc: 'SquareToRectangleAdapter') -> float:
    """
    Calculates the area of a rectangle-like object.
    
    Args:
        rc: An object with 'width' and 'height' attributes.
    
    Returns:
        float: The area of the rectangle (width * height).
    """
    return rc.width * rc.height

class SquareToRectangleAdapter:
    """
    Adapter class that adapts a Square to work with functions expecting rectangle-like objects.
    
    This adapter allows a Square object to be used wherever an object with 'width' and 'height'
    attributes is expected, without modifying the original Square class.
    """
    def __init__(self, square: Square):
        """
        Initialize the adapter with a Square object.
        
        Args:
            square (Square): The Square object to be adapted.
        """
        self.square = square

    @property
    def width(self) -> float:
        """
        Returns the width of the adapted square (equal to its side length).
        
        Returns:
            float: The side length of the square.
        """
        return self.square.side

    @property
    def height(self) -> float:
        """
        Returns the height of the adapted square (equal to its side length).
        
        Returns:
            float: The side length of the square.
        """
        return self.square.side