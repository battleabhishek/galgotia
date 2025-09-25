class Base1:
    def __init__(self):
        self.str1 = "Base1"
        print("Base1")

class Base2:
    def __init__(self):
        self.str2 = "Base2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def print_strs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.print_strs()

#create multiple in parents classes first secont and child class
class Parent1:
    def func1(self):
        print("This is son from Parent1")
class Parent2:
    def func2(self):
        print("This is daughter from Parent2")
        
class Child(Parent1, Parent2):
    def func3(self):
        print("This is born from Child")
# Example usage:
childObj = Child()
childObj.func1()  # Inherited from Parent1
childObj.func2()  # Inherited from Parent2
childObj.func3()  # Defined in Child

#class a and b are parent class and c is child class
class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
class B:
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(A, B):
    def feature5(self):
        print("Feature 5 is working")
#creating object of class c
obj = C()
obj.feature1()
obj.feature2()  
obj.feature3()
obj.feature4()
obj.feature5()