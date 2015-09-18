# how to define inner functions
def add_to(n):

	def adder(x):
		return n+x
		
	return adder
	
print(add_to(10)(3))

# create a decorator function
def add_positive(functie):

	def check_positive(args):
		for arg in args:
			if arg<0:
				raise ValueError(repr(arg) + " is not positive")
		return functie(args)
		
	return check_positive
	
# decorate a function
@add_positive
def adder(args):
	suma = 0
	for i in args:
		suma += i
	print("suma: ", suma)

adder([1,2])
#adder([-1,2])

# use more than one decorator
def add_integer(functie):

	def check_integer(args):
		for arg in args:
			if type(arg) == str:
				raise TypeError(repr(arg)+" is not an integer")
		return functie(args)
		
	return check_integer
	
@add_integer
@add_positive
def add_numbers(args):
	suma = 0
	for i in args:
		suma += i
	print("suma: ",suma)

add_numbers([1,4])	
#add_numbers(['',-2])

# decorate a class
def decorator(clasa):
	def inner():
		print("inner")
		return clasa
	return inner
	
@decorator
class my_class:
	
	value = "value"

	def __init__(self):
		print("init")

	@staticmethod
	def static_method_example():
		return "static method"

	@classmethod
	def class_method_example(cls):
		return cls.value

cl = my_class()
print(cl.static_method_example())
print(cl.class_method_example())


class Test:
	
	def __init__(self):
		self._valoare = None

	@property
	def valoare(self):
		return self._valoare
    
	@valoare.setter
	def valoare(self, val):
		self._valoare = val

test = Test()
print(test.valoare)
test.valoare = 10
print(test.valoare)