'''
85.	**Class** Car **and Inheritance**
•	Create a base class Car with attributes: make, model, year. 
    Create a derived class ElectricCar with an additional battery_size attribute.
'''
class car:                        # Created a normal class car with variables brand, model and year
    def __init__(self):            
        self.brand = "McLaren"
        self.model = "W1"
        self.year = 2024

class electricCar(car):           # Created derived class electricCar with additional attribute battery size
    def __init__(self):
        self.brand = "Tesla"
        self.model = "Model Y"
        self.year = 2019
        self.battery_size = "75 kWh"

GasCar = car()                    # Object of car class
print(GasCar.brand)               # printing the values
print(GasCar.model)
print(GasCar.year)

print()

E_Car = electricCar()            # Object of electricCar class
print(E_Car.brand)               # printing the values
print(E_Car.model)
print(E_Car.year)
print(E_Car.battery_size)