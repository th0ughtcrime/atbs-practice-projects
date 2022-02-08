# ATBS Ch. 5
# Fantasy Game Inventory
# List to Dictionary Function for Fantasy Game Inventory
#
# The 'display_inventory()' function takes a dictionary as an argument which
# symbolizes a game inventory, and prints the items and amounts of each, along
# with the total amount of all items.
#
# The `add_to_inventory()' function takes an inventory dictionary as an
# argument, same as above, and additionally a list with items which then adds
# to the initial inventory.

def display_inventory(inv: dict) -> None:
	print('Inventory:')

	item_total = 0
	for item, amount in inv.items():
		item_total += amount
		print(f'{amount} {item}')

	print(f'Total number of items: {item_total}\n')


def add_to_inventory(inv: dict, added_items: list) -> dict:
	# This for loop checks if an item already exists in the inventory, adds it
	# if it doesn't, and increments its value by 1 if it does.
	for item in added_items:
		inv.setdefault(item, 0)
		inv[item] += 1


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(stuff)
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
