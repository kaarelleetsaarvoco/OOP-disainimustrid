from adapter.adapter_class.adapter import SquareToRectangleAdapter

def calculate_area(rc: SquareToRectangleAdapter) -> float:
    """
    Calculates the area of a rectangle-like object.
    
    Args:
        rc: An object with 'width' and 'height' attributes.
    
    Returns:
        float: The area of the rectangle (width * height).
    """
    return rc.width * rc.height
