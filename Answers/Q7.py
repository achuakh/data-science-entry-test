class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    # using __init__ to define the class
    # with the following Args: 
    # make: The make of the car (e.g., "Toyota").
    # model: The model of the car (e.g., "Corolla").
    # year: The year the car was manufactured (e.g., 2020).
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Prints information about the car in the format "Year Make Model".    
    def describe_car(self):
        print(f"{self.make} {self.model} {self.year}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

# describe car 1
car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()

# describe car 2
car2 = Car("Land Rover", "Defender", 2002)
car2.describe_car()

print(f"Details of the best 4x4: {car2.make}, {car2.model}")
