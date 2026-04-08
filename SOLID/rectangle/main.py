from Rectangle import Rectangle
from Square import Square


def use_shape(shape):
    """
    Funktsioon, mis kasutab üldist Shape objekti.
    See funktsioon peab töötama korrektselt nii Rectangle kui Square objektidega,
    sest mõlemad järgivad Shape kontrakti (LSP).
    """
    print(f"\n{shape}")
    print(f"Area: {shape.area()}")


if __name__ == "__main__":
    # Loome ristküliku
    r = Rectangle(2, 3)
    print("=" * 40)
    print("RISTKÜLIK")
    print("=" * 40)
    use_shape(r)
    
    # Loome ruudu
    s = Square(5)
    print("\n" + "=" * 40)
    print("RUUT")
    print("=" * 40)
    use_shape(s)
    
    # Testime sõltumatut laiuse ja kõrguse muutmist (toimib ainult Rectangle puhul)
    print("\n" + "=" * 40)
    print("RISTKÜLIKU LAIUSE JA KÕRGUSE MUUTMINE")
    print("=" * 40)
    r.width = 4
    r.height = 6
    print(f"Pärast muutmist: {r}")
    print(f"Pindala: {r.area()}")
    
    # Testime ruudu suuruse muutmist (toimib ainult Square puhul)
    print("\n" + "=" * 40)
    print("RUUDU SUURUSE MUUTMINE")
    print("=" * 40)
    s.size = 7
    print(f"Pärast muutmist: {s}")
    print(f"Pindala: {s.area()}")
    
    print("\n" + "=" * 40)
    print("LSP JÄRGIMINE")
    print("=" * 40)
    print("Rectangle ja Square on mõlemad Shape objektid.")
    print("Kumbki neist ei riku teise käitumise eeldusi.")
    print("Igaüks neist järgib oma loogikat õigesti.")