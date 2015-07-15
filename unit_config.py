import Hero
import Monster

# ---create global monster and hero
monster = Monster.Monster()
monster.name = "Ravager"
hero = Hero.Hero()
# ---create global variables
monster_turn = True
done = False
dungeon = True
# ---create dungeon rooms
room_list=[]
current_room = 0
# Functions

def is_monster_dead():
    if monster.hp <= 0:
        # set dungeon to True to end combat loop
        return True

def is_hero_dead():
    if hero.hp <= 0 and not dungeon:
        # set combat loop to False and dungeon loop to False, ending the game
        return True
