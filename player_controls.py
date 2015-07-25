import unit_config


# ---DUNGEON CONTROLS---
# Perform action based on player_input
def dungeon_controls(player_input):
    if player_input == "NORTH" or player_input == "N":
        next_room = unit_config.room_list[unit_config.current_room].directions[0]
        if next_room is None:
            print("You can't go that way.")
        else:
            unit_config.current_room = next_room

    elif player_input == "EAST" or player_input == "E":
        next_room = unit_config.room_list[unit_config.current_room].directions[1]
        if next_room is None:
            print("You can't go that way.")
        else:
            unit_config.current_room = next_room

    elif player_input == "SOUTH" or player_input == "S":
        next_room = unit_config.room_list[unit_config.current_room].directions[2]
        if next_room is None:
            print("You can't go that way.")
        else:
            unit_config.current_room = next_room

    elif player_input == "WEST" or player_input == "W":
        next_room = unit_config.room_list[unit_config.current_room].directions[3]
        if next_room is None:
            print("You can't go that way.")
        else:
            unit_config.current_room = next_room
    # ---End Game---
    elif player_input == "QUIT" or player_input == "Q":
        print("Ending the game")
        unit_config.done = True

    # ---START DEBUG---
    elif player_input == "COMBAT" or player_input == "C":
        unit_config.dungeon = False
    # ---END DEBUG---

    # message when player enters a non existing command
    else:
        print("Player input invalid. Please try again.")


# ---END DUNGEON CONTROLS---


# ---COMBAT CONTROLS---
def get_player_input(player_input):
    if player_input == "ATTACK" or player_input == "A":
        unit_config.monster.takeDamage(unit_config.hero.heroAttack())


    elif player_input == "DEFEND" or player_input == "D":
        unit_config.hero.defence()
        print("you defend and prevent", unit_config.hero.defend, "damage")
        print()

    elif player_input == "HEAL" or player_input == "H":
        if unit_config.hero.potion > 0:
            unit_config.hero.heal()
        else:
            print("You are out of healing potions!")

    elif player_input == "FOCUS" or player_input == "F":
        unit_config.hero.heroFocus()
        if unit_config.hero.heroDead():
            unit_config.done = True
            print("You have died from over charging!")
        else:
            print("You change up an attack!")

    elif player_input == "QUIT" or player_input == "Q":
        print("Ending combat")
        unit_config.dungeon = True


    else:
        print("That input is invalid")
        unit_config.monster_turn = False


# ---END COMBAT CONTROLS---

