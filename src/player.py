# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items

    def __str__(self):
        return f'Player info: {self.name} : {self.currentRoom} : {self.items}'

# player = Player('carlitos', 'room', ['tools', 'shovel', 'pizza'])
# print(player)