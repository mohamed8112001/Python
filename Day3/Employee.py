import re
from Person import Person
from car import Car  

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, distanceToWork, salary):
        super().__init__(name, money, mood, healthRate)
        self.id = id

        #  Ensure car is a Car object
        if isinstance(car, Car):
            self.car = car
        else:
            raise TypeError(" Error: 'car' must be an instance of the Car class!")

        # Validate email
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            self.email = email
        else:
            raise ValueError(f" Invalid email: {email}")

        self.distanceToWork = distanceToWork
        self.salary = max(1000, salary)  # Ensures salary is at least 1000

    def work(self, hours):
        if hours == 8:
            self.mood = 'happy'
        elif hours > 8:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def drive(self, distance, velocity):
        if self.car.fuelRate > 0:
            self.car.run(velocity, distance)
        else:
            print(" Car has no fuel. Please refuel.")

    def refuel(self, gasAmount=100):
        if 0 <= self.car.fuelRate + gasAmount <= 100:
            self.car.fuelRate += gasAmount
            print(f" Car refueled. New fuel level: {self.car.fuelRate}%")
        else:
            print(" Invalid fuel amount. Fuel must be between 0 and 100.")

    def __str__(self):
        return f"{super().__str__()}, Salary: {self.salary}, Email: {self.email}, Car: {self.car}"

#  Create a Car object first
my_car = Car('BMW', 80, 120)  # Ensure Car class exists and works correctly

#  Pass the Car object to Employee
Employee1 = Employee('mohamed', 102, 'tired', 40, 1, my_car, 'mohamed@gmail.com', 200, 300)

Employee1.work(8)
print(Employee1)

Employee1.drive(100, 20)  #  Now this will work correctly
