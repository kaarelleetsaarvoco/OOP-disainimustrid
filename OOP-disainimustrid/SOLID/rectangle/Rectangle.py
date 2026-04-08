from shape import Shape


class Rectangle(Shape):
    """
    Ristkülik klassi loomine, mis esindab ristkülikut.
    Ristküliku laiust ja kõrgust saab muuta sõltumatult.
    """

    def __init__(self, width, height):
        """
        Konstruktor, mis võtab ristküliku laiuse ja pikkuse.
        
        Args:
            width: Ristküliku laius
            height: Ristküliku kõrgus
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Tagastab ristküliku laiuse."""
        return self._width
    
    @width.setter
    def width(self, value):
        """Seab ristküliku laiuse."""
        self._width = value
    
    @property
    def height(self):
        """Tagastab ristküliku kõrguse."""
        return self._height
    
    @height.setter
    def height(self, value):
        """Seab ristküliku kõrguse."""
        self._height = value

    def area(self):
        """Arvutab ristküliku pindala."""
        return self._width * self._height
    
    def __str__(self):
        """Tagastab ristküliku tekstilise kirjelduse."""
        return f"Rectangle - Width: {self._width}, Height: {self._height}"
    
