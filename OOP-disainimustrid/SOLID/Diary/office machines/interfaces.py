from abc import ABC, abstractmethod


class Printer(ABC):
    """Interface for printing functionality."""
    
    @abstractmethod
    def print(self, document):
        """Print a document."""
        pass


class Scanner(ABC):
    """Interface for scanning functionality."""
    
    @abstractmethod
    def scan(self, document):
        """Scan a document."""
        pass


class Fax(ABC):
    """Interface for faxing functionality."""
    
    @abstractmethod
    def fax(self, document):
        """Fax a document."""
        pass
