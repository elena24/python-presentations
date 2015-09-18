'''
KEYWORDS LIST IN PYTHON:

False        class        finally        is            return
None         continue     for            lambda        try
True         def          from           nonlocal      while
and          del          global         not           with
as           elif         if             or            yield
assert       else         import         pass
break        except       in             raise

'''

# as
import math as myMath
print(myMath.sqrt(4))

try:
    open("failFile.txt")
except FileNotFoundError as ex:
    print(ex)
finally:
    print("Finally")

# assert
def checkOdd(number):
    if number%2==0:
        return True
    else:
        return False


assert checkOdd(4) == True, "4 is odd"
assert checkOdd(3) == True, "3 is even"	# AssertionError

# break, continue
for i in range(5):
    if i==2:
        break
    print(i)
        
for i in range(5):
    if i==2:
        continue
    print(i)

# class, def, pass
class MyClass:
    def something():
        pass

# del
my_list = [1,2,3]
del my_list[0]
print(my_list)

a=3
print(a)
del a
print(a)      # NameError: name 'a' is not defined

# from, import
from keywords_example import myFunction
myFunction("aa")

# global
def example1():
    global ok
    ok = 1
    print('example1', ok)

def example2():
    global ok
    print('example2', ok)

example1()
example2()

# in
my_list = [1,2,3]
print(1 in my_list)
print(4 in my_list)
print('e' in 'hello')

# is
print([] is [])
print('' is '')

# lambda
a =  lambda x: x * x
for i in range(5):
   print(a(i))

# nonlocal
def outer():
    a = 1
    def inner():
        nonlocal a
        a=2
        print('inner',a)	# will print 2
    inner()
    print('outer',a)		# will print 2
outer()

# with
with open('D:\\keywords_test_file.txt', 'r') as f:
    line = f.read()
print(line)

# yield
def generator(maxim):
    for indice in range(maxim):
        yield indice

print(list(generator(5)))
