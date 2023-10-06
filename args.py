# *args =  parameter that will pack all arguments into a tuple
#          useful so that a function can accept a varying amount of arguments

def add(*stuff):  # args is short for arguments => *args = *stuff = *whatever
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


# def add(*whatever):  # args is short for arguments => *args = *stuff = *whatever
#     sum = 0
#     whatever = list(whatever)
#     whatever[0] = 0
#     for i in whatever:
#         sum += i
#     return sum


print(add(1, 2, 3, 4, 5, 6))
