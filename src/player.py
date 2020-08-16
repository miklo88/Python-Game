# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name=None, current_room=None, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.item = inventory

    def __str__(self):
        return f'Player info: Name: "{self.name}" Current Location: "{self.current_room}" Inventory Bag: "{self.inventory}"'

    def add_item(self):
        print(f'add_item worked for player')
        return self.item.append({self.current_room.item})

    # def drop_item(self):
    #     return self.item.remove()

 
# player = Player('carlitos', 'room', [])
# print(player)
# print(player.name)
# print(player.current_room)
# print(player.item)
