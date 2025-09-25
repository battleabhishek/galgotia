#file 1 mian.py
# a file name main.py is in same directory
from animal import animal
# get the module name of the imported class
print (f"the imported animal class is from module: {animal.__module__}")

# create instance and get its module name
my_animal = animal()
print (f"the instance of animal class is from module: {my_animal.__module__}")
print (f"the instance of animal class is from module: {animal().__module__}")

#animal.py
#A file named animmal.py
class animal:
    """A simple animal class"""
    def speak(self):
        print("Animal Speaking")
    def eat(self):
        print("Animal Eating")
    def sleep(self):
        print("Animal Sleeping")
    def __int__(self,Name):
        self.Name = Name
        print("Animal Created")
def get__module__name():
    return animal.__module__
if __name__ == "__main__":
    print(f"This class is defined in module:{animal__module__}")