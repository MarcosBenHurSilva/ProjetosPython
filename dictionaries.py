# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow',
            'Brasil': 'Brasília'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals['Brasil'])
print(capitals.get('Germany'))

for key, value in capitals.items():
    print(key, value)
