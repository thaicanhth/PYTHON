inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashe berry', 'list']
print(inventory)

inventory['backpack'] = sorted(inventory['backpack'])

print(inventory)

a = list(inventory['backpack'])
del a[2]

inventory['backpack'] = a
print(inventory)

inventory['gold'] += 50
print(inventory)
# dễ ra thi