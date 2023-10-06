# function + a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")


# hello("Marcos", "Silva", 31)
hello(input("What's your first name?: "), input("What's your last name?: "), input("How old are you?: "))
