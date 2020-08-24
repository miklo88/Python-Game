inventory = ['star','cone','circle','square','box']
item = input('add a string: ')
# print(item)
def drop_item(item):
    for i in inventory:
        if item != i:
            inventory.append(item)
        elif item['star'] == inventory[i]:
            inventory.remove('star')
        else:
            return f'failed'
    # for i in inventory:
    #     inventory.append(item)
    #     print(i)

    return f'{inventory}'
    
print(drop_item(item))
    