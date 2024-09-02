class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def createAutomobile():
    print("Enter the details of the automobile:")

    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    while True:
        doors = input("Number of doors: ")
        if doors in ['2', '4']:
            break
        else: print("Invalid number of doors. Please enter 2 or 4.")

    while True:
        roof = input("Type of roof (solid or sun roof): ")
        if roof in ['solid', 'sun roof']:
            break
        else: print("Invalid roof type. Please enter 'solid' or 'sun roof'.")

    car = Automobile(year, make, model, doors, roof)

    print("\nVehicle Details:")
    print(f"Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print(f"Roof: {car.roof}")

if __name__ == '__main__':
    while True:
        createAutomobile()
        if input("\nCreate another automobile? (y/n): ") == 'n':
            break