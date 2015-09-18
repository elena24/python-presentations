# single quotes
s1 = 'example1'
# double quotes
s2 = "example2"
s3 = "example\'example"     # will print example1'example2
s4 = "example\nexample"
print("s4:", s4)

# using raw string
s5 = "C:\name"
print("s5:", s5)
s6 = r"C:\name"
print("s6", s6)

# string formating
print("My name is %s and I am %d years old" % ("Elena", 23))
pi = 3.1415
print("pi = %1.2f" % (pi))
print("My name is {0} and I learn {1}".format("Elena", "Python"))
print("My name is {name} and I learn {something}".format(name="Elena", something="Python"))

# string with multiple lines
s7 = """
line1
line2
"""
print("s7", s7)


# string concatenation
s8 = 'Py' 'thon'            # will print Python
s9 = "Py" + "thon"          # will print Python
s10 = "Py" * 3 + "thon"     # will print PyPyPython
print("s10", s10)


# string slicing
word = "0123456789"
print(word[0])              # will print 0
print(word[-1])             # will print 9
print(word[0:2])            # will print 01
print(word[5:])             # will print 56789
print(word[0:8:2])          # will print 0246
print(word[::2])            # will print 02468
#print(word[12])             # IndexError: string index out of range

# strings are immutables
#word[0] = "2"               # TypeError: 'str' object does not support item assignment
