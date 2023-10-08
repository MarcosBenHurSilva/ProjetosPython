# if __name__ == '__main__'

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one which is __name__
# then Python will execute the code found within __main__

# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

if __name__ == '__main__':
    pass

print(__name__)

if __name__ == '__main__':  # testar rodando em outro modulo
    print("running this module directly")
else:
    print("running other module indirectly")


def main():
    print("Hello!")


if __name__ == '__main__':
    main()
