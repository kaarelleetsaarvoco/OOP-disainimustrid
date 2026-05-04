from abc import ABC, abstractmethod
from typing import List
from template.creature.creature import Creature

class CardGame(ABC):
    """
    Abstract base class that implements the Template Method pattern for card game combat.
    
    This class defines the general structure of combat between two creatures,
    while delegating specific behavior (hit implementation) to subclasses.
    """
    
    def __init__(self, creatures: List[Creature]):
        """
        Initialize the card game with a list of creatures.
        
        Args:
            creatures (List[Creature]): A list of creatures participating in the game.
        """
        self.creatures = creatures
    
    def combat(self, c1_index: int, c2_index: int) -> int:
        """
        Template Method that orchestrates the combat between two creatures.
        
        This method defines the general algorithm:
        1. Both creatures attack each other
        2. Check who survived
        3. Return the result
        
        The specific behavior of how damage is applied (hit method) is delegated to subclasses.
        
        Args:
            c1_index (int): Index of the first creature in the creatures list.
            c2_index (int): Index of the second creature in the creatures list.
        
        Returns:
            int: -1 if both creatures are alive or both are dead,
                 c1_index if only the first creature survived,
                 c2_index if only the second creature survived.
        """
        creature1 = self.creatures[c1_index]
        creature2 = self.creatures[c2_index]
        
        # Both creatures attack each other (delegates to subclass implementation)
        self.hit(creature1, creature2)
        self.hit(creature2, creature1)
        
        # Determine the outcome
        c1_alive = creature1.is_alive()
        c2_alive = creature2.is_alive()
        
        if c1_alive and not c2_alive:
            return c1_index
        elif c2_alive and not c1_alive:
            return c2_index
        else:
            # Both alive or both dead
            return -1
    
    @abstractmethod
    def hit(self, attacker: Creature, defender: Creature) -> bool:
        """
        Abstract method that must be implemented by subclasses.
        
        This method applies damage from the attacker to the defender.
        The specific behavior depends on the subclass implementation.
        
        Args:
            attacker (Creature): The creature dealing damage.
            defender (Creature): The creature taking damage.
        
        Returns:
            bool: True if the defender survived, False if the defender died.
        """
        pass
