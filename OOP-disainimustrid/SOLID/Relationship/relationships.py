from models import Relationship
from browser import RelationshipBrowser


class Relationships(RelationshipBrowser):
    """Manages relationships between people and provides a browser interface"""
    
    def __init__(self):
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        """Add a parent-child relationship"""
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
    
    def find_all_children_of(self, name):
        """
        Find all children of a person with the given name.
        
        Args:
            name: The name of the parent to search for
            
        Yields:
            Person objects who are children of the given parent
        """
        for person, relationship_type, related_person in self.relations:
            if person.name == name and relationship_type == Relationship.PARENT:
                yield related_person
