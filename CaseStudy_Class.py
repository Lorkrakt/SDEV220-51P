class Vehicle:
    def __init__(self,car):
        self.car = car


class Automobile(Vehicle):
    def __init__(self,year,make,model,door,roof,car):
        super().__init__(car)
        self.year = year
        self.make = make
        self.model = model
        self.doors = door
        self.roof = roof

        #gathers car info for output
    def get_vehicle_details(self):
        return f"Vehicle type: {self.car}\n" \
               f"Year: {self.year}\n" \
               f"Make: {self.make}\n"\
               f"Model: {self.model}\n" \
               f"Number of doors: {self.doors}\n" \
               f"Type of roof: {self.roof}"\
    
class VehicleApp:
    def __init__(self):
        pass

    def create_vehicle(self):
        try:
            #get vehicle details
            vehicle_car = input("What type of vehicle: ").lower()
                #check to make sure "car is input"
            if vehicle_car not in ["car"]:
                raise ValueError("Invalid type of vehicle. Please enter 'car'.")
            
            vehicle_year = int(input("What year of car? "))
            vehicle_make = input("What is the make of the car? ")
            vehicle_model = input("What is the model of the car? ")
            vehicle_door = int(input("How many doors does it have? "))
            vehicle_roof = input("What type of roof does it have?")

            #create vehicle instance

            vehicle = Automobile(car = vehicle_car,
                                 year = vehicle_year, 
                                 make = vehicle_make,
                                 model=vehicle_model, 
                                 door = vehicle_door, 
                                 roof = vehicle_roof )
            
            #display vehicle details
            print(vehicle.get_vehicle_details())
    
        except ValueError as e:
            print(f"Error: {e}")

app = VehicleApp()
app.create_vehicle()