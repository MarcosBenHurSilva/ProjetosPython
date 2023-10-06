from car import Car

car_1 = Car("Chevy", "Corvette", 2023, "blue")
car_2 = Car("Ford", "Mustang", 2024, "red")

# Car.wheels = 2
car_1.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()
