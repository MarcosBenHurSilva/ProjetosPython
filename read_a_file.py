try:
    with open('test2.txt') as file:  # o .txt está na página de projeto por isso não preciso do 'path'
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
