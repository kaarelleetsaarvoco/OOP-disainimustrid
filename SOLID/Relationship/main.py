from models import Person
from relationships import Relationships
from research import Research


# Main program
if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")
    
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)
    
    # Research accepts a RelationshipBrowser abstraction, not a concrete Relationships class
    Research(relationships)
