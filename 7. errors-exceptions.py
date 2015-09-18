import sys

# open a file that doesn't exist
try:
    open("file")
except IOError:
    print("No file")
else:
    print("File exists")
finally:
    print("finally")
    
print("Continue ")

# raise an exception
def raiseException(number):
    if number == 2:
        raise Exception("You have entered number 2")
    else:
        print("No exception")
    
try:
    raiseException(2)
except Exception as ex:
    print("exception: ", ex)
    
# create own exceptions:
class MyException(Exception):
    def __str__(self):
        return "MyException"

try:
    raise MyException()
except MyException as ex:
    print("Exception raised:", ex)
