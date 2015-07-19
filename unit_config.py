import Hero
import Monster

# ---create global monster and hero
monster = Monster.pick_monster(Monster.monster_list)
hero = Hero.Hero()
# ---create global variables
monster_turn = True
done = False
dungeon = True
# ---create dungeon rooms
room_list=[]
current_room = 0
# ---Functions
def monster_turn_check():
    # Check to see if hero is dead from posion or overcharge
    if hero.heroDead():
        pass
    # check to make sure player made legal action and give monster a turn
    elif monster_turn:
        # check that player has not defeted monster and check that player has not chosen to end game
        if not (monster.monsterDead() or dungeon):
            # Deal damage to hero
            hero.heroTakeDamage(monster.monsterAttack())
            # set hero.self.defend back to 0 for future rounds of combat
            hero.defend = 0
