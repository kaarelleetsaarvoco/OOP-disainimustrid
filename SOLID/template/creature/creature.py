class Creature:
    """
    Represents a creature in the card game with attack power and health points.
    """
    def __init__(self, attack: int, health: int):
        """
        Initialize a creature with attack power and health points.
        
        Args:
            attack (int): The amount of damage this creature deals when attacking.
            health (int): The current health points of the creature.
        """
        self.attack = attack
        self.health = health
        self.max_health = health
    
    def is_alive(self) -> bool:
        """
        Check if the creature is still alive.
        
        Returns:
            bool: True if health is greater than 0, False otherwise.
        """
        return self.health > 0
    
    def restore_health(self) -> None:
        """
        Restore the creature's health to its maximum value.
        """
        self.health = self.max_health
    
    def take_damage(self, damage: int) -> None:
        """
        Reduce the creature's health by the given damage amount.
        
        Args:
            damage (int): The amount of damage to take.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
