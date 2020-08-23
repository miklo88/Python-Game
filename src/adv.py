#ROOM IMPORT
from room import Room, room
#PLAYER IMPORT
from player import Player
#ITEM IMPORT
from item import Item, item
#TESTING PURPOSES
cubicle = Room('carls-room', 'bedroom that comes with some plants and a chonky cat.', ['beer', 'water', 'snacks'])
bag = Item('water', 'always be drinking that high quality h2o.')
print(cubicle.name)
print(cubicle.description)
print(cubicle.item)
print(bag.item_name)
print(bag.item_description)

# INSTRUCTIONS, PLAYER ENTER NAME, ININTIATE GAME
instructions = '''Welcome to the adventure game! You will be searching for a lost treasure. Using the keys on your keyboard of n, s, e, w 
you can control with cardinal direction your player travels! Good luck on your journey!'''
print(instructions)
# DECLARING PLAYER AS PLAYER() CLASS
player = Player()
# name = input(f'Enter your name: ')
name = 'Carl' #remove when you want to test the entire flow////////!
# PLAYER.NAME
player.name = name
# PLAYER.CURRENT_ROOM
player.current_room = room['outside']
# PLAYER.INVENTORY
player.inventory = item['watch']

# print(room.item)
print(player.inventory)
#PLAYER.CURRENT_ROOM.ITEM
print(f'////// {player} end player info//////')

# ///// INVOKING THE GAME
while True:
# PLAYERS CURRENT_ROOM
    print(f'{player.current_room.name}')
# ROOM DESCRIPTION
    print(f'{player.current_room.description}')
# ROOM ITEMS IF ANY
    print(f'{player.current_room.item}')

#GAME NAVIGATION
    direction = input('Move by cardinal direction commands n, s, e or w. You can "grab item" or "drop item": ')
    
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
