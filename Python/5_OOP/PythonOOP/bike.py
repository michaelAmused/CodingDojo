class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        info = { 'Price': self.price, 'Max_Speed': self.max_speed, 'Miles': self.miles }
        return info

    def ride(self):
        self.miles += 10
        return "Riding"

    def reverse(self):
        if self.miles >0:
            self.miles -= 5
        return "Reversing"

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "15mph")
bike3 = Bike(300, "30mph")

print bike1.ride()
print bike1.ride()
print bike1.ride()
print bike1.reverse()
print bike1.displayInfo()

print bike2.ride()
print bike2.ride()
print bike2.reverse()
print bike2.reverse()
print bike2.displayInfo()

print bike3.reverse()
print bike3.reverse()
print bike3.reverse()
print bike3.displayInfo()
