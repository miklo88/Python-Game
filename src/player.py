# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room=None, item=[]):
        self.name = name
        self.current_room = current_room
        self.item = item

    def add_item(self):
        return item.append()

    def drop_item(self):
        return item.remove()

    def __str__(self):
        return f'Player info: {self.name} : {self.current_room} : {self.item}'

# player = Player('carlitos', 'room', ['inventory', 'shovel', 'pizza'])
# print(player)
# print(player.item)
