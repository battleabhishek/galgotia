# function in firstfile.py
def my_function():
    print("Hello from my_function!called from firstfile.py")
#check the value of __name__
if __name__ == "__main__":
    print(f"the name of the module is {__name__}")
    print("firstfile.py is being run directly")
else:
    print(f"the name of the module is {__name__}")
    print("firstfile.py is being imported")
