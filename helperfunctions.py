# Shinaola Agbede
#################
# Helper functions to improve main readability
def main_menu(curr_room):
    print("Main menu")
    print("You are in: {}".format(curr_room))
    print("1. Scan room for items")
    print("2. Check backpack")
    print("3. Scan room for exit")
    print("4. Show current room")
    print("5. Move rooms")
    print("6. Quit game")

def item_menu():
    list_items()
    print("Items menu")
    print("1. Grab Item")
    print("2. Exit")

def glork_menu():
    print("Uh-oh! The Glork is here!")
    print("1. Fight")
    print("2. Escape")

def room_menu(curr_room, rooms):
    print("Current Room: {}".format(curr_room))
    print("1. Scan for items")
    print("2. Scan for exit")

def exit_menu():
    print('You found the exit! This is your chance to escape!')
    print('1. Take exit')
    print('2. Not take the exit')

# shuffles the glork to new rooms
def shuffle_glork(glork_position, rooms):
    print('Glork shuffle!')

# glork battle functions
# execute when user decides to try to escape
def escape_glork():
    pass

# execute when user decides to fight glork
def fight_glork():
    pass

# shuffles the items to new rooms
def shuffle_items(item_list, room_list, items):
    pass

def list_items(curr_room, rooms):
    return rooms[curr_room]

# scans the input room -> returns boolean
def scan_room(room, rooms):
    return list_items(room, rooms) != None

# scans the room for exit -> returns boolean
def find_exit(room):
    pass

# to show rooms adjacent to current room
def show_adj_rooms(curr_room, rooms):
    return rooms[curr_room]

def check_backpack(bakpak):
    return bakpak.values()