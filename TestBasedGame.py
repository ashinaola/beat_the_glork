# Shinaola N. Agbede
#####################

import helperfunctions
import random
import time

def scan_room(player_room, item_placement, ROOMS):
    print("You are in: {}".format(player_room))
    print('Listing items...')
    time.sleep(2)
    if player_room in item_placement.values():
        print(helperfunctions.list_items(player_room, ROOMS))
        helperfunctions.item_menu()

def check_backpack(backpack):
    print('Checking backpack from items...')
    time.sleep(1)
    print(helperfunctions.check_backpack(backpack))

def scan_exit(player_room, exit_location):
    print("You are in: {}".format(player_room))
    print("Scanning room...")
    time.sleep(1)
    if helperfunctions.find_exit(player_room, exit_location):
        helperfunctions.exit_menu()
        user_decision = int(input())
        if user_decision == 1:
            print('You Escaped the Compund! You win!')
        else:
            print('You decided against leaving.')

def move_rooms(glork_room, item_placement, ROOMS):
    helperfunctions.shuffle_glork(glork_room, ROOMS)
    helperfunctions.shuffle_items(list(item_placement.values()))
    print('Showing connected rooms...')
    print(helperfunctions.show_adj_rooms(player_room, ROOMS))
    while user_decision not in helperfunctions.show_adj_rooms(player_room, ROOMS):
        user_decision = input('Moving rooms...Please select room:')
    player_room = user_decision

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
    item_placement = { item:room for (item,room) in zip(item_rooms, ITEMS) }
    print(item_placement)
    backpack = {}

    # Start game
    user_decision = 0

    while user_decision != 6:
        # check for glork
        print('FOO item_loc: {}'.format(item_rooms))
        if glork_room == player_room:
            user_decision = int(input(helperfunctions.glork_menu()))
            if user_decision == 1:
                fight_res = helperfunctions.fight_glork(backpack)
                if fight_res == True:
                    print("You have defeated the glork! You win!")
                    break
                else:
                    print("The glork has devored you. You lose..")
                    break
            elif user_decision == 2:
                esc_res = helperfunctions.escape_glork(backpack)
                if esc_res == True:
                    print('You have escaped the glork!')
                    print('keep going!')
                else:
                    print('The glork has caught you. You lose!')
                    break
            else:
                print('Wrong input, enter 1 or 2...')
        # display main menu and take in user input
        else:
            helperfunctions.main_menu(player_room)
            user_decision = int(input())

            # branching based on user decision
            match user_decision:
                case 1: # option -> scan room
                    scan_room(player_room, item_placement, ROOMS)

                case 2: # option -> check backpack
                    check_backpack(backpack)

                case 3: # option -> scan exit
                    scan_exit(player_room, exit_location)

                case 4: # option -> check current location
                    print('You are in: {}'.format(player_room))

                case 5: # option -> move rooms
                    move_rooms(glork_room, item_placement, ROOMS)

if __name__ == "__main__":
    main() 