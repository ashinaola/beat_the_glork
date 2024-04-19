# Shinaola N. Agbede
#####################

import helperfunctions
import random
import time

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
    ITEMS = ['Potion', 'Raygun', 'jet-pack', 'Unpotion']
    player_room = 'Main'
    init_room_selec = list(ROOMS.keys())
    init_room_selec.remove("Main")
    exit_location = random.choice(init_room_selec)
    glork_room = random.choice(init_room_selec)
    item_rooms = random.sample(init_room_selec, 4)
    print('FOO: {}'.format(item_rooms))
    item_placement = { item:room for (item,room) in zip(item_rooms, ITEMS) }
    print(item_placement)
    backpack = {}

    # Start game
    user_decision = 0

    while user_decision != 5:
        # check for glork
        if glork_room == player_room:
            helperfunctions.glork_menu()
        # display main menu and take in user input
        helperfunctions.main_menu(player_room)
        user_decision = int(input())

        # branching based on user decision
        match user_decision:
            case 1: # option -> scan room
                print("You are in: {}".format(player_room))
                print('Listing items...')
                time.sleep(2)
                print(helperfunctions.list_items())

            case 2: # option -> scan exit
                print("You are in: {}".format(player_room))
                print("Scanning room...")
                time.sleep(2)
                if helperfunctions.find_exit(player_room):
                    helperfunctions.exit_menu()
                    user_decision = int(input())
                    if user_decision == 1:
                        print('You Escaped the Compund! You win!')
                    else:
                        print('You decided against leaving.')

            case 3: # option -> check current location
                print('You are in: {}'.format(player_room))

            case 4: # option -> move rooms
                # shuffle the glork
                helperfunctions.shuffle_glork(glork_room)
                # shuffle the items
                helperfunctions.shuffle_items(item_placement)
                # show the adjacent rooms
                print('Showing connected rooms...')
                print(helperfunctions.show_adj_rooms(player_room, ROOMS))
                # take in user input
                user_decision = input('Please select')
                # set player room to selected
                player_room = user_decision

if __name__ == "__main__":
    main() 