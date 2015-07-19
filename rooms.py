import unit_config
import player_controls
import dungeon
import Monster

dungeon.dungeon(dungeon.dungeon_one)


# ---Dungeon Loop
def dungeon_loop():
    """
    started with game, will be changed later to reflect different areas
    :return: void
    """
    while unit_config.dungeon and not unit_config.done:
        print(unit_config.room_list[unit_config.current_room][0])
        player_input = input("Which way would you like to go?: ")
        print()
        player_input = player_input.upper()

        # Perform action based on player_input
        player_controls.dungeon_controls(player_input)


# ---combat_loop
def combat_loop():
    """
    started when a player encounters a monster
    :rtype : void
    """
    if not unit_config.dungeon and not unit_config.done:
        print("You encounter ", unit_config.monster.name, "!")

    while not unit_config.dungeon and not unit_config.done:
        # Prevents monster from taking a turn if player does not input a valid command (see unit_config.monster_turn_
        # check)
        unit_config.monster_turn = True
        # Get player actions
        player_input = input("What would you like to do?: ")
        player_input = player_input.upper()
        print()

        # Perform action based on player input/decision
        player_controls.get_player_input(player_input)

        # Check to see if monster is still alive so it does not get a turn
        if unit_config.monster.monsterDead():
            unit_config.dungeon = True
            print("You defeted the ", unit_config.monster.name, "!")

        # ----Monster Turn-----
        unit_config.monster_turn_check()

        # Check to make sure the hero is still alive
        if unit_config.hero.heroDead():
            unit_config.done = True
            print("The monster has defeted you!")
