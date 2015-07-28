import unit_config
import player_controls
import game_dungeons




# ---Dungeon Loop
def dungeon_loop():
    """
    started with game, will be changed later to reflect different areas
    :return: void
    """
    unit_config.room_list = game_dungeons.dungeon_one.load_dungeon()
    while unit_config.dungeon and not unit_config.done:
        print(unit_config.room_list[unit_config.current_room].name)
        player_input = input("Which way would you like to go?: ")
        print()
        player_input = player_input.upper()

        # Perform action based on player_input
        player_controls.dungeon_controls(player_input)

        # Checks if there is a monster in the rooms and starts combat
        if not unit_config.room_list[unit_config.current_room].no_monster:
            unit_config.dungeon = False

# ---combat_loop
def combat_loop():
    """
    started when a player encounters a monster
    :rtype : void
    """


    monster = unit_config.monster_create()
    unit_config.monster = monster
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
            print("You defeated the ", unit_config.monster.name, "!")

        # ----Monster Turn-----
        # Check to see if hero is dead from poison or overcharge
        if unit_config.hero.heroDead():
            pass

        # check to make sure player made legal action and give monster a turn
        elif unit_config.monster_turn:
            # check that player has not defeated monster and check that player has not chosen to end game
            if not (unit_config.monster.monsterDead() or unit_config.dungeon):
                # Deal damage to hero
                unit_config.hero.heroTakeDamage(unit_config.monster.monsterAttack())
                # set hero.self.defend back to 0 for future rounds of combat
                unit_config.hero.defend = 0

        # Check to make sure the hero is still alive
        if unit_config.hero.heroDead():
            unit_config.done = True
            print("The monster has defeated you!")
