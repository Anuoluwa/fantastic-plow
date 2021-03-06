"""
OOP = modeling object 
"""

""" 
Challenge
Use the planning strategy and process demonstrated above to design a parking lot. This is a common OOP interview question and the time you spend thoughtfully thinking through this problem will be helpful.

As you design your solution, and think through all of the necessary objects, attributes, methods, and relationships, keep the following in mind:

Payments
What methods are allowed?
Where do customers pay?
Capacity
How does the system respond when the lot is full?
How does the system know when the lot is full?
Vehicles
Is capacity allocated differently depending on what type of vehicle enters the lot? How so?
Pricing
Are there different rates for different times of day? How will this be handled?
Is there a discount for purchasing a longer total time?

++++++++
Nouns(Classes) : User, Payments, Capacity, Vehicles, Pricing
Adverbs(Attributes):  
Payments
    vehicles details()
    channels: cash, card, e-transfer
    amount: 

Capacity:
    total_lots
    entry_time
    exit_time

Vehicles:
    VIN
    color
    license
    brand
    Type
Pricing:
    duration:
    price_per_durations:
    Capacity()

Methods:
Vehicles:
    drive_in
    drive_out
Relationships
vehicle car 


"""

from datetime import datetime

class User:
    def __init__(self, name,):
        self.name = name
        self.phone = phone

class Capacity:
    def __init__(self, total_lots):
        self.total_lots = total_lots

class Payment:
    def __init__(self, channel):
        self.channel = channel
        self.amount = 0

class Vehicle:
    def __init__(self, vehicle_license, color, maker, brand):
        self.license = license
        self.color = color
        self.maker = maker
        self.brand = brand
    
    def get_vehicle(self):
        return  
class Staff(User):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.park_lot = 0
        self.vehicle = []
    
    def create_park_lot(total_lots, self):
        park_lot = Capacity(total_lots)


    def get_vehicle_details(self, vehicle_license, color, maker, brand):
        vehicle = Vehicle(vehicle_license, color, maker, brand, self)



class Driver(User):
    def __init__(self, name, phone):
        super().__init__(name, phone)

    
class Pricing:
    def  __init__(self, rate_per_min, entry_time, exit_time):
        self.rate_per_min = rate_per_min
        self.entry_time = datetime.now()
        self.exit_time = datetime.now()


    def calculate_amount(self):
        total_time = entry_time - exit_time
        amount = rate_per_min * total_time
