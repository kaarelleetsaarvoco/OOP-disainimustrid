from specification import Specification


class BetterFilter:
    """
    Parandatud filtriklass, mis järgib OCP (Open/Closed Principle) printsiipi
    
    BetterFilter teab ainult, kuidas rakendada spetsifikatsioone.
    See ei sisalda konkreetset teadmist värvide, suuruste ega nimede kohta.
    """
    
    def filter(self, items, spec):
        """
        Filtreerib items spetsifikatsiooni järgi, kasutades generaatorit
        
        Args:
            items: iterable objektide kogum
            spec: Specification objekt, mis määrab filtreerimise tingimused
            
        Yields:
            Objektid, mis rahuldavad spetsifikatsiooni
        """
        for item in items:
            if spec.is_satisfied_by(item):
                yield item
