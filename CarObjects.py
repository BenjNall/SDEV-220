#defines a superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#defines a subclass Automobile of the superclass Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#function to create an automobile object
def createAutomobile():
    print("Enter the details of the automobile:")

    #input details of the automobile
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    #validate the number of doors to 2 or 4
    while True:
        doors = input("Number of doors: ")
        if doors in ['2', '4']:
            break
        else: print("Invalid number of doors. Please enter 2 or 4.")

    #validate the type of roof to solid or sun roof
    while True:
        roof = input("Type of roof (solid or sun roof): ")
        if roof in ['solid', 'sun roof']:
            break
        else: print("Invalid roof type. Please enter 'solid' or 'sun roof'.")

    #create an automobile object
    car = Automobile(year, make, model, doors, roof)

    #display the details of the automobile
    print("\nVehicle Details:")
    print(f"Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print(f"Roof: {car.roof}")

#main code
if __name__ == '__main__':
    #create automobile objects until the user wants to stop
    while True:
        createAutomobile()
        if input("\nCreate another automobile? (y/n): ") == 'n':
            break