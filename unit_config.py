import Hero
import Monster
# ---create global monster and hero

def monster_create():
    """ picks a random monster from the list and returns it
    :rtype : object
    :return: object
    """
    monster_new = Monster.pick_monster(Monster.monster_list)
    return monster_new

monster = monster_create()

hero = Hero.Hero()
# ---create global variables
monster_turn = True
done = False
dungeon = True
# ---create dungeon rooms
room_list = []
current_room = 0
