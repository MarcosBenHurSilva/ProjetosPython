# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are know as the function's return value.

def multiply(number1, number2):
    return number1 * number2


# x = multiply(6, 8)
x = multiply(int(input("Digite o 1º número: ")), int(input("Digite o 2º número: ")))

print(x)
