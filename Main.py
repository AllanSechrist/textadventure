import unit_config
import rooms

__author__ = 'Allan'


# -------Main program loop-------
while not unit_config.done:
    rooms.dungeon_loop()
    # if player has encountered a monster, end dungeon loop and start combat loop
    rooms.combat_loop()
