# Multilevel Inheritance Example in Python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def cute(self):
        print("Puppy is cute")

# Example usage:
p = Puppy()
p.speak()   # Inherited from Animal
p.bark()    # Inherited from Dog
p.cute()    # Defined in Puppy



#create multi level inheritance for electronics device portable device and laptop
class Electronics:
    def power_on(self):
        print("Electronics device is powered on")
    def power_off(self):
        print("Electronics device is powered off")
class PortableDevice(Electronics):
    def carry(self):
        print("Carrying the portable device")
class Laptop(PortableDevice):
    def code(self):
        print("Coding on the laptop")
# Example usage:
laptop = Laptop()
laptop.power_on()   # Inherited from Electronics
laptop.carry()      # Inherited from PortableDevice
laptop.code()       # Defined in Laptop
