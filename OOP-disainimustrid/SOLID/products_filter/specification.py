from abc import ABC, abstractmethod
from product import Color, Size


class Specification(ABC):
    """Abstraktne baasklass spetsifikatsioonidele"""
    
    @abstractmethod
    def is_satisfied_by(self, item):
        """
        Kontrollib, kas item rahuldab spetsifikatsiooni
        
        Args:
            item: kontrollitav item
            
        Returns:
            True, kui item rahuldab tingimuseid, vastasel juhul False
        """
        pass
    
    def __and__(self, other):
        """
        Võimaldab kombineerida spetsifikatsioone & operaatori abil
        
        Args:
            other: teine Specification
            
        Returns:
            AndSpecification kombinatsioon
        """
        return AndSpecification(self, other)


class ColorSpecification(Specification):
    """Spetsifikatsioon värvile"""
    
    def __init__(self, color):
        """
        Konstruktor
        
        Args:
            color: soovitud värv (Color enum)
        """
        self.color = color
    
    def is_satisfied_by(self, item):
        """Kontrollib, kas item on soovitud värviga"""
        return item.color == self.color


class SizeSpecification(Specification):
    """Spetsifikatsioon suurusele"""
    
    def __init__(self, size):
        """
        Konstruktor
        
        Args:
            size: soovitud suurus (Size enum)
        """
        self.size = size
    
    def is_satisfied_by(self, item):
        """Kontrollib, kas item on soovitud suurusega"""
        return item.size == self.size


class NameSpecification(Specification):
    """Spetsifikatsioon nimele"""
    
    def __init__(self, name):
        """
        Konstruktor
        
        Args:
            name: soovitud nimi (osalised nimed lubatud)
        """
        self.name = name
    
    def is_satisfied_by(self, item):
        """Kontrollib, kas item nimes sisaldab etteantud sõne"""
        return self.name.lower() in item.name.lower()


class AndSpecification(Specification):
    """Kombineeritud spetsifikatsioon - mõlemad tingimused peavad olema täidetud"""
    
    def __init__(self, first, second):
        """
        Konstruktor
        
        Args:
            first: esimene Specification
            second: teine Specification
        """
        self.first = first
        self.second = second
    
    def is_satisfied_by(self, item):
        """Kontrollib, kas item rahuldab mõlemat spetsifikatsiooni"""
        return self.first.is_satisfied_by(item) and self.second.is_satisfied_by(item)
