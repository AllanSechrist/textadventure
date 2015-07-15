import unit_config



dungeon_one = []
room = ["Entrance. You feel the breeze from the outside and the smell of earth fills your nose, you can only move south",
        None, None, 1, None]
dungeon_one.append(room)
room = ["Room 1, you can move north or east", 0, 2, None, None]
dungeon_one.append(room)
room = ["Room 2, you can move south or west", None, None, 3, 1]
dungeon_one.append(room)
room = ["Room 3, you can move north or south", 2, None, 4, None]
dungeon_one.append(room)
room = ["Room 4, you can move north or east", 3, 5, None, None]
dungeon_one.append(room)
room = ["Room 5, you can move east or west", None, 6, None, 4]
dungeon_one.append(room)
room = ["Room 6, you can move north or west", 7, None, None, 5]
dungeon_one.append(room)
room = ["Room 7, you can move north or south", 8, None, 6, None]
dungeon_one.append(room)
room = ["Room 8, you can move east or south", None, 9, 7, None]
dungeon_one.append(room)
room = ["Room 9, you can move north or west", 10, None, None, 8]
dungeon_one.append(room)
room = ["Room 10, you can only move south", None, None, 9, None]
dungeon_one.append(room)

def dungeon(dungeon_number):
    unit_config.room_list = dungeon_number
