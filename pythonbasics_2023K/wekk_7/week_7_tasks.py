
# 1. complex class with attributes a, b and i, and get & set methods
class Complex:

    i = "i" #root of -1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a   
    
    def getB(self):
        return self.b

    def setA(self, a):
        self.a = a   
    
    def setB(self, b):
        self.b = b

# 2.Clock class, alarm subclass, method ticking and alarming
class Clock:
    def __init__(self, name):
        self.name = name
    def Ticking(self):
        print("tick.... tick.... tick... ")

class AlarmClock(Clock):
    def __init__(self, name):
        super().__init__(name)

    def Alarm(self):
        print("ALARM!... Alarm! ...")

# 3. migratory bird oop, bird has name, ammount of eggs 1-10 
# and migratory ? has country (starts with capital letter, 5 -20 letters)and month(1 -12) atrributes
class Bird:
    def __init__(self, name, eggs):
        self.name = name
        if 1 <= eggs <= 10:
            self.eggs = eggs
        else:
            self.eggs = 1

class Migratory(Bird):
    def __init__(self, name, eggs, country, month):
        Bird.__init__(self,name,eggs)
        if(5 <= len(country) <= 20):
            self.country = country.capitalize()
        else:
            self.country = ""
        if(1 <= month <= 12):
            self.month = month
        else:
            self.month = 0

clock_1 = Clock("first_clock")
clock_2 = AlarmClock("second_clock")

clock_1.Ticking()
clock_2.Alarm()
