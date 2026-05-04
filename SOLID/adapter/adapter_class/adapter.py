from adapter.square.square import Square

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
