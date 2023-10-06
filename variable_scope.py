# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created
# LEBG => L = local > E = enclosing > G = global > B = Built-in

name = "Marcos"  # global scope (available inside & outside this function)


def display_name():
    name = "Ben-hur"  # local scope (available only inside this function)
    print(name)


display_name()
print(name)
