import unit_config
import rooms
"""
# ---VARIABLES AND CONTROLS---

# variable for main program loop
unit_config.done = False
# variable for dungeon loop, checks if player is not in combat
unit_config.dungeon = True
# set room
unit_config.current_room = 0
# ---END VARIABLES AND CONTROLS
"""

# -------Main program loop-------
while not unit_config.done:
    rooms.dungeon_loop()
    # if player has encountered a monster, end dungeon loop and start combat loop
    rooms.combat_loop()
