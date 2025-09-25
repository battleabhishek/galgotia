class MyClass:
    def greet(self): # method definition with self parameter
        print("Hello! welcome")# method body

    def personalized_greet(self, name):# method with additional parameter
        print(f"Hello, {name}!")# using f-string for formatting

    def call_greet(self):# function taking method as argument
        self.greet()# calling method inside function
    def call_greet(self):  # method inside the class
        self.greet()  # calling another method

# creating object of class
obj = MyClass()
# calling method:
print(obj.greet())# calling method without argument
print(obj.personalized_greet("Vikash"))#using method with argument
print(obj.call_greet())# calling method


