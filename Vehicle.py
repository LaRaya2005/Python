from car import Car

car_1 = Car("Chevy","Covevette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()