from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstraktne baasklass, mis esindab üldist kujundit.
    Kõik kujundid peavad teadma oma pindala arvutamist.
    """
    
    @abstractmethod
    def area(self):
        """
        Arvutab kujundi pindala.
        """
        pass
    
    @abstractmethod
    def __str__(self):
        """
        Tagastab kujundi tekstilise kirjelduse.
        """
        pass
