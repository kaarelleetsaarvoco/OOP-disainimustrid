def is_singleton(factory):
    """
    Check if a factory function returns a Singleton object.
    
    A factory is a Singleton if it always returns the exact same object
    when called multiple times.
    
    Args:
        factory: A callable that creates/returns an object
        
    Returns:
        True if the factory always returns the same object (Singleton)
        False if the factory returns different objects each time
    """
    # Create the first object
    obj1 = factory()
    
    # Create a second object
    obj2 = factory()
    
    # Check if both objects are the same object in memory
    # Use 'is' operator to check identity, not equality
    return obj1 is obj2


# Example 1: Singleton class
class Database:
    """Singleton database class"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def create_db():
    """Factory function that creates a Database Singleton"""
    return Database()


# Example 2: Non-Singleton class
class User:
    """Regular User class (not a Singleton)"""
    pass


def create_user():
    """Factory function that creates new User objects"""
    return User()


# Test the is_singleton function
if __name__ == "__main__":
    print("Testing Singleton Pattern Detection:")
    print()
    
    # Test 1: Database is a Singleton
    result1 = is_singleton(create_db)
    print(f"is_singleton(create_db): {result1}")
    print("Expected: True")
    print()
    
    # Test 2: User is not a Singleton
    result2 = is_singleton(create_user)
    print(f"is_singleton(create_user): {result2}")
    print("Expected: False")
