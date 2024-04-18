# Shinaola N. Agbede
#####################

import helperfunctions
import random

# main method
def main():
    # set up the board
    ROOMS = {
        'Main': ['Room 6', 'Room 4', 'Room 1', 'Room 3'],
        'Room 1': ['Main'],
        'Room 2': ['Room 3', 'Main'],
        'Room 3': ['Room 2'],
        'Room 4': ['Main', 'Room 5'],
        'Room 5': ['Room 4'],
        'Room 6': ['Main', 'Room 7'],
        'Room 7': ['Room 6']
    }
    player_room = 'Main'
    exit_location = random.choice(list(ROOMS.keys()))
    glork_room = random.choice(list(ROOMS.keys()))
    numb_of_items = random.randint(1,7)
    item_locs = [random.choice(list(ROOMS.keys())) for i in range(numb_of_items)]
    print(exit_location)

    # Start game
    start_decision = 0

    while start_decision != 4:
        start_decision = int(input(helperfunctions.main_menu()))

        match start_decision:
            case 1: # scan room
                helperfunctions.scan_room(player_room)
                pass
            case 2: # scan for exit
                helperfunctions.find_exit(player_room)
                pass
            case 3: # move rooms
                pass
            case 4:
                break

if __name__ == "__main__":
    main() 