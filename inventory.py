import pprint

def display_inventory(inventory): 
    total = 0
    for k, v in inventory.items():
        print( str(k) + ':\t\t' + str(v))
        total += v
    print('Total:\t\t' + str(total))

inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)

def add_to_inventory(inventory, item_list):
    for item in item_list:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
