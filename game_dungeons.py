import dungeon

"""
A file to store all the dungeons in the game, hence, game_dungeons
"""


dungeon_one = dungeon.Dungeon(name="dungeon one", rooms=[

    ["Entrance. You feel the breeze from the outside and the smell of earth fills your nose, you can only move south",
     None, None, 1, None],

    ["Room 1, you can move north or east", 0, 2, None, None],

    ["Room 2, you can move south or west", None, None, 3, 1],

    ["Room 3, you can move north or south", 2, None, 4, None],

    ["Room 4, you can move north or east", 3, 5, None, None],

    ["Room 5, you can move east or west", None, 6, None, 4],

    ["Room 6, you can move north or west", 7, None, None, 5],

    ["Room 7, you can move north or south", 8, None, 6, None],

    ["Room 8, you can move east or south", None, 9, 7, None],

    ["Room 9, you can move north or west", 10, None, None, 8],

    ["Room 10, you can only move south", None, None, 9, None]
])