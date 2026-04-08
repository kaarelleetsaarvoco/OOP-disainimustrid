from machine import Machine


class OldFashionedPrinter(Machine):
    """An old-fashioned printer that only supports printing."""
    
    def print(self, document):
        """Print a document."""
        print(f"Printing: {document}")
    
    def fax(self, document):
        """Faxing is not supported - do nothing."""
        pass
    
    def scan(self, document):
        """Scanning is not supported - raise an error."""
        raise NotImplementedError("Printer cannot scan!")
