from item import Item, item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name=None, current_room=None, item=[]):
        self.name = name
        self.current_room = current_room
        self.item = item

    def __str__(self):
        return f'Player info: Player Name: "{self.name}" Current Location: "{self.current_room}" Inventory Bag: "{self.item}"'

    def add_item(self):
        # print(f'add_item worked for player', {self.player.inventory})
        return self.item

    def drop_item(self):
        return self.item.remove()

# player = Player('carlitos', 'room', ['something cool'])
# print(player)
# print(player.name)
# print(player.current_room)
# print(player.item)
# player.item.append('caprisun')
# player.item.append('pop-tarts')
# player.item.remove('something cool')

# print(player)

