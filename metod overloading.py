#method overloading in multilvel inheritence simple non loop
class A():
    def method(self):
        print("method of class A")
class B(A):
    def method(self):
        print("method of class B")
class C(B):
    def method(self):
        print("method of class C")

obj1=A()
obj1.method()
obj2=B()
obj2.method()
obj3=C()
obj3.method()

#method overloading in multilvel inheritence with loop
class A():
    def method(self):
        print("method of class A")
class B(A):
    def method(self):
        print("method of class B")
        super().method()
class C(B):
    def method(self):
        print("method of class C")
        super().method()

obj1=A()
obj1.method()
obj2=B()
obj2.method()
obj3=C()
obj3.method()

    
        
        