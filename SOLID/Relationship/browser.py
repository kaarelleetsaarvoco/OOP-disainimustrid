from abc import ABC, abstractmethod


class RelationshipBrowser(ABC):
    """Abstract base class defining the interface for browsing relationships"""
    
    @abstractmethod
    def find_all_children_of(self, name):
        """
        Find all children of a person with the given name.
        
        Args:
            name: The name of the parent to search for
            
        Returns:
            A collection of Person objects who are children of the given parent
        """
        pass
