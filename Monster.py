import random


class Monster():
    # ---constructor---
    def __init__(self):
        self.name = ""
        self.hp = 0 + random.randrange(50, 81)
        self.attack = 5
        self.speed = random.randrange(11)

    # ---Methods---


    def takeDamage(self, damage):
        # Calculates hp to be reduced when hero attacks
        self.hp -= damage
        print("Monster took", damage, "damage")
        if self.hp > 0:
            print(str(self.hp), "hit points remaining")
        else:
            print("The monster has no hit points left!")
        print()

    def monsterAttack(self):
        # Return attack damage to be dealt to hero
        return self.attack + random.randrange(3, 6)
