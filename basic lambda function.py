#basic lambada functin add map filter shorted
#syntax
#lambda argument:expression
#example
#addfunction
def add(x):
    return x+10
print(add(5))
#using lambda function
x=lambda a:a+10
print(x(5))
y=lambda a,b:a*b
print(y(5,6))
#using lambda function with map
lst=[1,2,3,4,5]
newlist=list(map(lambda x:x**2,lst))
print(newlist)
#using lambda function with filter
lst=[1,2,3,4,5,6,7,8,9,10]
evenlist=list(filter(lambda x:(x%2==0),lst))
print(evenlist)
#using lambda function with sorted
lst=[('apple',2),('banana',3),('orange',1)]
sortedlist=sorted(lst,key=lambda x:x[1])
print(sortedlist)
#using lambda function with reduce
from functools import reduce
lst=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,lst)
print(sum)
#using lambda function with list comprehension
lst=[1,2,3,4,5]
newlist=[(lambda x:x*2)(x) for x in lst]
print(newlist)
#using lambda function with if else
lst=[1,2,3,4,5,6,7,8,9,10]
newlist=[(lambda x:x*2 if x%2==0 else x*3)(x) for x in lst]
print(newlist)
#using lambda function with nested function
def outerfunc(n):
    return lambda x:x*n 
doubler=outerfunc(2)
tripler=outerfunc(3)
print(doubler(5))
print(tripler(5))
#using lambda function with class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name:{self.name},Age:{self.age}')
    def birthday(self):
        self.age=(lambda x:x+1)(self.age)
p=Person('John',25)
p.display() 
p.birthday()
p.display()
#using lambda function with exception handling
def divide(a,b):
    try:
        result=(lambda x,y:x/y)(a,b)
        return result
    except ZeroDivisionError:
        return 'Error: Division by zero'
print(divide(10,2))
print(divide(10,0)) 
#using lambda function with recursion
factorial=(lambda f:lambda x:1 if x==0 else x*f(f)(x-1))(lambda f:lambda x:1 if x==0 else x*f(f)(x-1))
print(factorial(5))

