# map() = applies a function to each item in a iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_reais = lambda data: (data[0], data[1] * 5)
to_dollars = lambda data: (data[0], data[1] / 5)

store_reais = list(map(to_reais, store))
store_dollars = list(map(to_dollars, store))

for i in store_reais:
    print(i)
print("---------------------------")
for i in store_dollars:
    print(i)
