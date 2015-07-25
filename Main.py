import unit_config
import rooms

__author__ = 'Allan'

print(unit_config.room_list)
# -------Main program loop-------
while not unit_config.done:
    rooms.dungeon_loop()
    # if player has encountered a monster, end dungeon loop and start combat loop
    rooms.combat_loop()
    # DEBUG
    break