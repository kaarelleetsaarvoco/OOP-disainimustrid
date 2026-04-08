from product import Product, Color, Size
from filter import BetterFilter
from specification import ColorSpecification, SizeSpecification, NameSpecification


if __name__ == "__main__":
    # Toodete loomine
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
    
    products = [apple, tree, house]
    
    # BetterFilter instantsieerimine
    bf = BetterFilter()
    
    # Roheline värv filtreerimine
    print("Rohelised tooted:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} on roheline")
    
    print()
    
    # Suur suurus filtreerimine
    print("Suured tooted:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} on suur")
    
    print()
    
    # Kombineeritud tingimus: suur JA sinine
    print("Suured sinised tooted:")
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} on suur ja sinine")
    
    print()
    
    # Nime järgi filtreerimine
    print("Nimes sisaldub 'Tree':")
    tree_name = NameSpecification("Tree")
    for p in bf.filter(products, tree_name):
        print(f" - {p.name}")
    
    print()
    
    # Kompleksne kombinatsioon: roheline VÕI (roheline JA väike)
    print("Kõik tooted (näide):")
    for p in products:
        print(f" - {p}")
