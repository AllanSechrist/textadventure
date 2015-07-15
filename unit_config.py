import Hero
import Monster

#---create global monster and hero
monster = Monster.Monster()
monster.name = "Ravager"
hero = Hero.Hero()
#---create global variables
monster_turn = True
done = False
dungeon = True
combat = False
#---create dungeon rooms
room_list=[]
current_room = 0

