# slicing = create a substring by extracting elements from another string
#           indexing[]          or      slice()
#           [start:stop:step]           start:stop:step)

name = "Marcos Silva"

first_name = name[:6]       # [0:6]
last_name = name[7:]        # [7:end]
funky_name = name[::2]      # [0:end:2]
reversed_name = name[::-1]  # [0:end:-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
