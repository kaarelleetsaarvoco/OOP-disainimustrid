class Machine:
    """Base class for all office machines."""
    
    def print(self, document):
        """Print a document."""
        raise NotImplementedError("print() method not implemented")
    
    def fax(self, document):
        """Fax a document."""
        raise NotImplementedError("fax() method not implemented")
    
    def scan(self, document):
        """Scan a document."""
        raise NotImplementedError("scan() method not implemented")
