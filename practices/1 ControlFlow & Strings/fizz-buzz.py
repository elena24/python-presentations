"""
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5; 
The number as a string for other cases.

Input: A number as an integer.
Output: The answer as a string.

"""

def checkio(number):
    #replace this for solution
    pass

#These "asserts" using only for self-checking
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
