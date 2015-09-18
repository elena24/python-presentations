"""
Open a file

open(filename, mode)
mode = w -> write
       r -> read
       r+ -> read/write
       b -> binary
"""
f = open("D:\\Python\\files\\ex1.txt", "r+")

"""
read from a file
"""
print(f.read())     # print all file
print(f.readline()) # print one line

"""
write in a file
"""
print(f.write('test'))      # returns number of characters written


print(f.tell())         # returns the current position in file
f.seek(5)               # change the current position
print(f.tell())         # will print 5

"""
close file
"""
f.close()
