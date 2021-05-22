class Car_truck:
    def __init__(self, type, max_over, min_over, weight_truck, travel_time):
        self.type = type
        self.max_over = max_over
        self.min_over = min_over
        self.weight_truck = weight_truck
        self.travel_time = travel_time

def __str__ (self):
    return f"{self.max_over}, {self.min_over}, {self.weight_truck}, {self.travel_time} "

def type_truck (self, name):
    self.type += name
    if self.type ==  "Mersedes - Benz"  or "Reno":
         return name
    else:
        print("Not truck")


def overclocking (self, value):
    if value == int:
        self.min_over += value
        if self.min_over <= self.max_over and self.min_over > 0:
            print("Permissible speed")
        else:
            print("Unacceptable speed")
    else:
        raise TypeError

try:
    overclocking()
except TypeError as a:
    print("Not a number", a)

import datetime
def time_work (self, time_start):
    now = datetime.datetime.today().strftime("%H%M%S")
    start = datetime.datetime(time_start).strftime("%H%M%S")
    result = now - start
    write_time_in_doc()
    return result

def write_time_in_doc (result):
    with open("time_in_way.txt", "a") as a:
        a.write(result)


def weight_with_cargo (self, cargo):
    total_weight = weight_truck + cargo
    return total_weight