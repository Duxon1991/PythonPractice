
class Vehicle:

    def __init__(self,name,max_speed, mileage):
        self.name = name
        self.maxspeed = max_speed
        self.mileage = mileage

    def drive(self):
        print('vrooooooom!')

    def seating_capacity(self,capacity):
        print(f"Vehicle is {self.name} and the seating capacity is {capacity} !")

BMW = Vehicle('BMW',150,50000)
print(BMW.maxspeed, BMW.mileage)


class Bus(Vehicle):
    pass

DoubleDecker = Bus('volvo',70,200000)
print(DoubleDecker.maxspeed, DoubleDecker.mileage)
DoubleDecker.drive()
DoubleDecker.seating_capacity(150)
