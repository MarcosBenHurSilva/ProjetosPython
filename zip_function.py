# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["01/01/2021", "01/02/2021", "01/03/2021"]

users1 = zip(usernames, passwords, login_date)
print(type(users1))

for i in users1:
    print(i)

users2 = dict(zip(usernames, passwords))

print(type(users2))

for key, value in users2.items():
    print(key + ": " + value)
