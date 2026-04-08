from machine import Machine


class MultiFunctionPrinter(Machine):
    """A multi-function printer that supports all operations."""
    
    def print(self, document):
        """Print a document."""
        print(f"Printing: {document}")
    
    def fax(self, document):
        """Fax a document."""
        print(f"Faxing: {document}")
    
    def scan(self, document):
        """Scan a document."""
        print(f"Scanning: {document}")
