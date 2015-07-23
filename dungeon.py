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

    def __init__(self, name="", north=0, east=0, south=0, west=0, monster=False, item=False):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.monster = monster
        self.item = item

    # CLASS METHODS


#unit_config.room_list = dungeon_one.load_dungeon()