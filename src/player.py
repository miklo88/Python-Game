from item import Item, item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name=None, current_room=None, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'Player info: Player Name: "{self.name}" Current Location: "{self.current_room}" Inventory Bag: "{self.inventory}"'

    def add_item(self):
        # self.inventory.append()
        #adding an item to my list in Player object. so. 
        #need a data type {item} 
        return self.item

    # def drop_item(self):
    #     return self.inventory.remove()
        # return f'drop_item {self.inventory}'


player = Player('carlitos', 'room', ['something cool'])
print(player)
print(player.name)
print(player.current_room)
print(player.inventory)
# print(item)
player.inventory.append('caprisun')
player.inventory.append('pop-tarts')
# player.inventory.remove('something cool')
print(player.inventory)
player.drop_item()

print(player)

