# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true

# while 1==1:
#    name = print("help! I'm stuck in a loop!")

name = ""

while not name:  # = while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)

