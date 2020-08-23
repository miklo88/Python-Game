# room class import
from room import Room, room
# player class import
from player import Player
# item import
from item import Item, item
#
# Main
#
instructions = '''Welcome to the adventure game! You will be searching for a lost treasure. Using the keys on your keyboard of n, s, e, w 
you can control with cardinal direction your player travels! Good luck on your journey!'''
print(instructions)

# Make a new player object that is currently in the 'outside' room.
player = Player()
# name = input(f'Enter your name: ')
name = 'Carl'
player.name = name
player.current_room = room['outside']
# print(player.current_room.item)
player.inventory = item['watch']

# print('player.current_room.item', player.current_room.item)
print(player.inventory)
# print(f'////// {player} end player info//////')

# Write a loop that:
while True:
# # * Prints the current room name
    print(f'{player.current_room.name}')
# # * Prints the current description (the textwrap module might be useful here).
    print(f'{player.current_room.description}')
    #prints items in a room if any
    print(f'{player.current_room.item}')
    # print(f'{player.current_room.item.item_name}')
# If the user enters a cardinal direction, attempt to move to the room there.
    direction = input('Move by cardinal direction commands N, S, E or W. You can "grab item" or "drop item": ')
    # Print an error message if the movement isn't allowed.
    if direction == 'n':
        if player.current_room is not None:
            player.current_room = player.current_room.n_to 
    #handle error
    elif direction == 's':
        if player.current_room is not None:
            player.current_room = player.current_room.s_to
    #handle error
    elif direction == 'e':
        if player.current_room is not None:
            player.current_room = player.current_room.e_to
    #handle error
    elif direction == 'w':
        if player.current_room is not None:
            player.current_room = player.current_room.w_to
#handle error
#grabbing an item
    elif direction == 'grab item':
        item_name = player.current_room.item
        # print('//// item_name ///',item_name)
        # grabbing the item using get item from room class
        item = player.current_room.get_item(item_name)
        # print('//// item_name whole item ///',item)
        if item:
            # invokes ontake from item class so you know you have it
            item.on_take()
#removing from room
            # AttributeError: 'Item' object has no attribute 'remove'
            player.current_room.remove_item(item)
            print('/// room without item',item)
            print('/// current room item', player.current_room.item)
            # print('/// player inventory', player.inventory)
            #removing from room and adding to players inventory
            player.inventory.append(item)
            print('/// player inventory', player.inventory)
        # print('grabbed some stuff')
        else:
            print(f'{item_name} ////// is not here.')
        # if direction == 'grab item':
        
#dropping the item
    elif direction == 'drop item':
        print('drop some stuff')

# If the user enters "q", quit the game.
    elif direction == 'q':
        print(f'Sadly the quest has ended.')
        break
# * Waits for user input and decides what to do.
    else:
        print(f'Wrong way. Try again.')
