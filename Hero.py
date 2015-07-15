import random


class Hero():
    #---constructor---
    def __init__(self):
        self.name = "Link"
        self.hp = 100
        self.attack = 5
        self.defend = 0
        self.potion = 3
        self.focus = 0
        self.speed = random.randrange(11)
    #---Methods---
    def heroTakeDamage(self, damage):
        self.hp -= damage
        print("Monster" + " attacks you for " + str(damage))
        print("You have", str(self.hp), "hit points left")
        print()

    def heroAttack(self):
        #Calculate and return damage to be dealt to monster
        self.total = self.attack + (random.randrange(0, 5))
        if self.focus > 0:
            self.total = (self.total * 2 * self.focus)
        self.focus = 0
        return self.total

    def defence(self):
        #Allow player to pass turn and reduce incoming damage
        self.defend += random.randrange(2, 5)

    def heal(self):
        #Allow player to heal themselves, also increases defence for a turn
        recover = 10 + random.randrange(5, 11)
        self.hp += recover
        self.potion -= 1
        self.defend += random.randrange(1, 4)
        print("You recover : " + str(recover) + " hp")

    def heroFocus(self):
        #Allow player to increase next attack's damage
        self.focus += 1
