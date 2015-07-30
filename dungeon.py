import unit_config


class Room:
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
        # getter methods
    def combat(self):
        return self.no_monster

    def item(self):
        return self.item
        # end getter methods

class Dungeon:
    """
    CONSTRUCTOR
    Create a Dungeon object with a name and rooms
    """

    def __init__(self, name="", rooms=[]):
        self.name = name
        self.rooms = rooms

    # CLASS METHODS
        # "getter" methods
    def load_dungeon(self):
        return self.rooms

    def get_size(self):
        return len(self.rooms)

        # end getter methods

    def add_room(self, name, directions, no_monster, item):
        self.rooms.append(Room(name, directions, no_monster, item))