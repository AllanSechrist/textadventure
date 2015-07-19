import random


class Monster():
    # ---constructor---
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp + random.randrange(50, 81)
        self.attack = attack + random.randrange(1, 6)
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

    def monsterDead(self):
        if self.hp <= 0:
            return True

# List of Monsters
monster_list = []
ravager = Monster("Ravager", random.randrange(50, 61), random.randrange(5, 8))
monster_list.append(ravager)
bat = Monster("Bat", -30, 3)
monster_list.append(bat)
kobold = Monster("Kobold", -10, 5)
monster_list.append(kobold)
slime = Monster("Slime", random.randrange(10, 25), random.randrange(6, 10))
monster_list.append(slime)


# pick a monster
def pick_monster(list):
    """
    picks a monster to generate at random for combat
    :rtype : object
    """
    return list[random.randrange(0, len(list))]
