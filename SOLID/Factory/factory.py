class Person:
    """Represents a person with an ID and name"""
    
    def __init__(self, id, name):
        """
        Initialize a Person.
        
        Args:
            id: The unique identifier for this person
            name: The name of this person
        """
        self.id = id
        self.name = name


class PersonFactory:
    """Factory for creating Person objects with auto-incremented IDs"""
    
    def __init__(self):
        """Initialize the factory with ID counter starting at 0"""
        self._id_counter = 0
    
    def create_person(self, name):
        """
        Create a new Person object with an automatically assigned ID.
        
        Args:
            name: The name of the person to create
            
        Returns:
            A new Person object with the next sequential ID
        """
        person = Person(self._id_counter, name)
        self._id_counter += 1
        return person


# Example usage
if __name__ == "__main__":
    factory = PersonFactory()
    
    p1 = factory.create_person("Anna")
    p2 = factory.create_person("Mark")
    
    print(p1.id, p1.name)
    print(p2.id, p2.name)
