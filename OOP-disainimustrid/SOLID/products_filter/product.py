from enum import Enum


class Color(Enum):
    """Värvide Enum"""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Size(Enum):
    """Suuruste Enum"""
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Product:
    """Toote klass"""
    
    def __init__(self, name, color, size):
        """
        Konstruktor
        
        Args:
            name: toote nimi
            color: toote värv (Color enum)
            size: toote suurus (Size enum)
        """
        self.name = name
        self.color = color
        self.size = size
    
    def __repr__(self):
        return f"Product(name='{self.name}', color={self.color.name}, size={self.size.name})"
