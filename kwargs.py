# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
# kwargs = keywords arguments

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Marcos", middle="da", last="Silva")
