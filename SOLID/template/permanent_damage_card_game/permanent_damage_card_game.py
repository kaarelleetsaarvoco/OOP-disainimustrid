from template.card_game.card_game import CardGame
from template.creature.creature import Creature

class PermanentDamageCardGame(CardGame):
    """
    Card game variant where damage is permanent.
    
    In this game, damage accumulates. Once a creature takes damage,
    their health does not recover for future combats.
    """
    
    def hit(self, attacker: Creature, defender: Creature) -> bool:
        """
        Apply damage from attacker to defender with permanent damage rules.
        
        The defender takes damage equal to the attacker's attack power.
        The damage is permanent and does not recover.
        
        Args:
            attacker (Creature): The creature dealing damage.
            defender (Creature): The creature taking damage.
        
        Returns:
            bool: True if the defender survived, False if the defender died.
        """
        # Apply damage (permanent)
        defender.take_damage(attacker.attack)
        
        # Return whether defender is still alive
        return defender.is_alive()
