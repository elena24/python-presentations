
def test_if(x):
    if x == 0:
        print("zero")
    elif x % 2 == 0:
        print("even number")
    else:
        print("odd number")
        
    a, b = 0, 1
    print("foo" if a<b else "bar")
    
def test_for(word):
    for s in word:
        print(s)
    
def test_while(number):
    while number >= 0:
        print(number)
        number -= 1

def test_for_else():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

if __name__ == '__main__':
    #test_if(10)
   # test_for("abc")
  #  test_while(4)
    test_for_else()
