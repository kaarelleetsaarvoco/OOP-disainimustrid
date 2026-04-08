from devices import MyPrinter, OldFashionedPrinter, SimpleScanner, Photocopier, MultiFunctionMachine


def main():
    print("=" * 60)
    print("Interface Segregation Principle - Office Machines Example")
    print("=" * 60)
    
    # Test 1: Simple Printer
    print("\n1. MyPrinter (implements Printer interface only)")
    print("-" * 60)
    printer = MyPrinter()
    printer.print("Hello from MyPrinter")
    # printer.scan() — would cause an error, as expected, since MyPrinter doesn't implement Scanner
    
    # Test 2: Old-Fashioned Printer
    print("\n2. OldFashionedPrinter (implements Printer interface only)")
    print("-" * 60)
    old_printer = OldFashionedPrinter()
    old_printer.print("Document from old-fashioned printer")
    # No scan() method - no need for empty or error-throwing methods!
    
    # Test 3: Simple Scanner
    print("\n3. SimpleScanner (implements Scanner interface only)")
    print("-" * 60)
    scanner = SimpleScanner()
    scanner.scan("Important document to scan")
    # No print() method - scanner is just a scanner
    
    # Test 4: Photocopier
    print("\n4. Photocopier (implements Printer and Scanner interfaces)")
    print("-" * 60)
    photocopier = Photocopier()
    photocopier.print("Copy this document")
    photocopier.scan("Original document to copy")
    
    # Test 5: Multi-Function Machine (using composition)
    print("\n5. MultiFunctionMachine (composition-based)")
    print("-" * 60)
    print("Creating a multi-function machine with:")
    print("  - MyPrinter as the printing component")
    print("  - SimpleScanner as the scanning component")
    
    mfm = MultiFunctionMachine(
        printer=MyPrinter(),
        scanner=SimpleScanner()
    )
    
    print("\nDelegating print operation:")
    mfm.print("Document 1 for printing")
    
    print("\nDelegating scan operation:")
    mfm.scan("Document 1 for scanning")
    
    # Test 6: Multi-Function Machine with Photocopier
    print("\n6. MultiFunctionMachine (using Photocopier as both printer and scanner)")
    print("-" * 60)
    mfm2 = MultiFunctionMachine(
        printer=Photocopier(),
        scanner=Photocopier()
    )
    
    print("\nUsing photocopier for printing:")
    mfm2.print("Document 2 for printing")
    
    print("\nUsing photocopier for scanning:")
    mfm2.scan("Document 2 for scanning")
    
    print("\n" + "=" * 60)
    print("Summary: ISP benefits demonstrated")
    print("=" * 60)
    print("""
Key Points:
✓ MyPrinter only implements Printer - no unnecessary methods
✓ SimpleScanner only implements Scanner - focused responsibility
✓ Photocopier implements both Printer and Scanner - as needed
✓ No empty methods or artificial NotImplementedError
✓ Each class has exactly the methods it needs
✓ MultiFunctionMachine uses composition instead of inheritance
✓ Code is cleaner, more maintainable, and follows ISP
    """)


if __name__ == "__main__":
    main()
