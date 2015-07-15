import unit_config
import player_controls


room = ["Main Hall. You can move north, east, or west", 3, 1, None, 8]
unit_config.room_list.append(room)
room = ["Dining Area. You can move north or east.", 4, None, None, 0]
unit_config.room_list.append(room)
room = ["Master Bedroom. You can move north, east or south.", 5, 3, 8, None]
unit_config.room_list.append(room)
room = ["Living room. You can move in any direction.", 6, 4, 0, 2]
unit_config.room_list.append(room)
room = ["Kitchen. You can move north, south or west.", 7, None, 1, 3]
unit_config.room_list.append(room)
room = ["Bathroom. You can move east or south.", None, 6, 2, None]
unit_config.room_list.append(room)
room = ["Guest Bedroom. You can move east, south or west.", None, 7, 3, 5]
unit_config.room_list.append(room)
room = ["Back yard. You can move south and west.", None, None, 4, 6]
unit_config.room_list.append(room)
room = ["Family room. You can move north and east.", 2, 0, None, None]
unit_config.room_list.append(room)


# Functions to check for death of monster and hero
def is_monster_dead():
    if unit_config.monster.hp <= 0:
        print("You defeted the ", unit_config.monster.name, "!")
        # set dungeon to True to end combat loop
        unit_config.dungeon = True

def is_hero_dead():
    if unit_config.hero.hp <= 0 and not unit_config.dungeon:
        print("The monster has defeted you!")
        # set combat loop to False and dungeon loop to False, ending the game
        unit_config.dungeon = True
        unit_config.done = True




# ---Dungeon Loop
def dungeon_loop():
    while unit_config.dungeon and not unit_config.done:
        print(unit_config.room_list[unit_config.current_room][0])
        player_input = input("Which way would you like to go?: ")
        print()
        player_input = player_input.upper()

        # Perform action based on player_input
        player_controls.dungeon_controls(player_input)


# ---combat_loop
def combat_loop():
    if not unit_config.dungeon and not unit_config.done:
        print("You encounter ", unit_config.monster.name, "!")

    while not unit_config.dungeon and not unit_config.done:
        unit_config.monster_turn = True
        player_input = input("What would you like to do?: ")
        player_input = player_input.upper()
        print()

        # Perform action based on player input/decision
        player_controls.get_player_input(player_input)

        # Check to see if monster is still alive so it does not get a turn
        is_monster_dead()

        # ----Monster Turn-----
        player_controls.monster_turn_check()

        # Check to make sure the hero is still alive
        is_hero_dead()
