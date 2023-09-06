def displayInventory(inventory):
	print("Inventory:")
	total = 0
	if type(inventory) is not dict:
		print("Total number of items:", total)
		return
	
	for item, count in inventory.items():
		print(count, item)
		total += count

	print("Total number of items:", total)
	print("-" * 60)

def addToInventory(inventory, addedItems):
	if type(inventory) is not dict or type(addedItems) is not list:
		return

	newInventory = inventory.copy()
	for item in addedItems:
		if item not in newInventory.keys():
			newInventory.setdefault(item, 0)
		newInventory[item] += 1

	return newInventory


if __name__ == "__main__":
	stuff = { 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
	displayInventory(stuff)
	print()

	inv = {'gold coin': 42, 'rope': 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	displayInventory(inv)
	newInv = addToInventory(inv, dragonLoot)
	displayInventory(newInv)