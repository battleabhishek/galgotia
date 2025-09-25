# secondfile.py
from firstfile import my_function
my_function()
# secondfile.py
if __name__ == "__main__":
    print("secondfile.py is being run directly")
# secondfile.py
else:
    print("secondfile.py is being imported")

# secondfile.py
import firstfile
print(f"Accessing my_function from secondfile.py:")
print("the value of __name__ in secondfile.py is:", __name__)
firstfile.my_function()