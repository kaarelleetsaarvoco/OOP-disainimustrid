from template.card_game.card_game import CardGame
from template.creature.creature import Creature

class TemporaryDamageCardGame(CardGame):
    """
    Card game variant where damage is temporary.
    
    In this game, if a creature survives an attack, its health is restored to full.
    Only death is permanent - regular damage does not carry over to the next turn.
    """
    
    def hit(self, attacker: Creature, defender: Creature) -> bool:
        """
        Apply damage from attacker to defender with temporary damage rules.
        
        The defender takes damage equal to the attacker's attack power.
        If the defender survives, their health is restored to maximum.
        
        Args:
            attacker (Creature): The creature dealing damage.
            defender (Creature): The creature taking damage.
        
        Returns:
            bool: True if the defender survived, False if the defender died.
        """
        # Apply damage
        defender.take_damage(attacker.attack)
        
        # If defender is still alive, restore health to maximum
        if defender.is_alive():
            defender.restore_health()
            return True
        else:
            return False
