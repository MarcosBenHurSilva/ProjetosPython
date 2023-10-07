# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters: expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(int(input("Digite um número: "))))
print(multiply(int(input("Digite o 1º número: ")), int(input("Digite o 2º número: "))))
print(add(int(input("Digite o 1º número: ")), int(input("Digite o 2º número: ")), int(input("Digite o 3º número: "))))
print(full_name(input("Digite seu nome: "), input("Digite seu sobrenome: ")))
print(age_check(int(input("Digite a sua idade: "))))
