import dungeon

"""
A file to store all the dungeons in the game, hence, game_dungeons
"""

dungeon_one = dungeon.Dungeon(name="dungeon one", rooms=[])

room0 = dungeon.Room("Entrance. You feel the breeze from the outside and the smell of earth fills your nose, you can "
                     "only move south",
                     [None, None, 1, None], True, False)
dungeon_one.rooms.append(room0)

room1 = dungeon.Room("Room 1, you can move north or east", [0, 2, None, None], True, False)
dungeon_one.rooms.append(room1)

room2 = dungeon.Room("Room 2, you can move south or west", [None, None, 3, 1], False, False)
dungeon_one.rooms.append(room2)

room3 = dungeon.Room("Room 3, you can move north or south", [2, None, 4, None], True, False)
dungeon_one.rooms.append(room3)

room4 = dungeon.Room("Room 4, you can move north or east", [3, 5, None, None], True, False)
dungeon_one.rooms.append(room4)

room5 = dungeon.Room("Room 5, you can move east or west", [None, 6, None, 4], True, False)
dungeon_one.rooms.append(room5)

room6 = dungeon.Room("Room 6, you can move north or west", [7, None, None, 5], True, False)
dungeon_one.rooms.append(room6)

room7 = dungeon.Room("Room 7, you can move north or south", [8, None, 6, None], True, False)
dungeon_one.rooms.append(room7)

room8 = dungeon.Room("Room 8, you can move east or south", [None, 9, 7, None], True, False)
dungeon_one.rooms.append(room8)

room9 = dungeon.Room("Room 9, you can move north or west", [10, None, None, 8], True, False)
dungeon_one.rooms.append(room9)

room10 = dungeon.Room("Room 10, you can only move south", [None, None, 9, None], True, False)
dungeon_one.rooms.append(room10)

