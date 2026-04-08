from shape import Shape


class Square(Shape):
    """
    Ruudu klassi loomine, mis esindab ruutu.
    Ruudus on kõik küljed võrdsed.
    Square EI peri Rectanglest - see on iseseisev klass, mis pärib Shape klassist.
    """

    def __init__(self, size):
        """
        Konstruktor, mis võtab ruudu suuruse.
        
        Args:
            size: Ruudu külje pikkus
        """
        self._size = size

    @property
    def size(self):
        """Tagastab ruudu külje pikkuse."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Seab ruudu külje pikkuse."""
        self._size = value

    def area(self):
        """Arvutab ruudu pindala."""
        return self._size * self._size
    
    def __str__(self):
        """Tagastab ruudu tekstilise kirjelduse."""
        return f"Square - Size: {self._size}"



