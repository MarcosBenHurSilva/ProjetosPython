# logical operators (and, or, mot) = used to check if two or more conditional statement is true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp<= 30:
    print("the temperature is goood today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
