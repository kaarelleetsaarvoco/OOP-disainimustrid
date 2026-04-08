from interfaces import Printer, Scanner, Fax


class MyPrinter(Printer):
    """Simple printer that only supports printing."""
    
    def print(self, document):
        """Print a document."""
        print(f"Printing: {document}")


class OldFashionedPrinter(Printer):
    """Old-fashioned printer that only supports printing."""
    
    def print(self, document):
        """Print a document."""
        print(f"Printing (old-fashioned): {document}")


class SimpleScanner(Scanner):
    """Simple scanner that only supports scanning."""
    
    def scan(self, document):
        """Scan a document."""
        print(f"Scanning: {document}")


class Photocopier(Printer, Scanner):
    """Photocopier that supports both printing and scanning."""
    
    def print(self, document):
        """Print a document."""
        print(f"Photocopier printing: {document}")
    
    def scan(self, document):
        """Scan a document."""
        print(f"Photocopier scanning: {document}")


class MultiFunctionMachine(Printer, Scanner, Fax):
    """Multi-function machine that delegates printing, scanning, and faxing to separate components."""
    
    def __init__(self, printer, scanner, fax=None):
        """
        Initialize the multi-function machine with separate components.
        
        Args:
            printer: Object implementing the Printer interface
            scanner: Object implementing the Scanner interface
            fax: Optional object implementing the Fax interface
        """
        self.printer = printer
        self.scanner = scanner
        self.fax_machine = fax
    
    def print(self, document):
        """Delegate printing to the printer component."""
        self.printer.print(document)
    
    def scan(self, document):
        """Delegate scanning to the scanner component."""
        self.scanner.scan(document)
    
    def fax(self, document):
        """Delegate faxing to the fax component if available."""
        if self.fax_machine is not None:
            self.fax_machine.fax(document)
        else:
            print(f"Faxing not available: {document}")
