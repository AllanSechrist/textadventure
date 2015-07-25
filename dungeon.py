import unit_config


class Dungeon():
    """
    CONSTRUCTOR
    Create a Dungeon object with a name and rooms
    """

    def __init__(self, name="", rooms=[]):
        self.name = name
        self.rooms = rooms

    # CLASS METHODS

    def load_dungeon(self):
        return self.rooms


class Room():
    """
    CONSTRUCTOR
    Create a room with the possible directions to move, items and monsters
    """

    def __init__(self, name="", directions=[], no_monster=True, item=False):
        self.name = name
        self.directions = directions
        self.no_monster = no_monster
        self.item = item

    # CLASS METHODS

    def combat(self):
        return self.no_monster

    def item(self):
        return self.item


#unit_config.room_list = dungeon_one.load_dungeon()