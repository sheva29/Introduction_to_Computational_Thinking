import math
# x = 0.0
# numIters = 100000
# for i in range(numIters):
#     x += 0.1
# print(x) #prints 10000.0, because print automatically rounds
# print(repr(x))
# print(10.0*x == numIters)

# Use this when you comparing 2 floating points
# def close(x, y, epsilon = 0.00001):
#     return abs(x - y) < epsilon

# if close(10.0*x, numIters):
#     print('Good enough')

def isPal(x):
    """requires x to be a list
    returns True if the list is a palindrome; False otherwise"""
    assert type(x) == list
    temp = x[:]
    print(temp)
    temp.reverse()
    print("temp:", temp)
    print("x:", x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """requires: n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
    assert type(n) == int and n > 0
    result = []
    for i in range(n):
        elem = input('Enter something: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Is a palindrome')
    else:
        print('Is not a palindrome')

def isPalTest():
    L = [1, 2]
    result = isPal(L)
    print('Should print False:', result)
    L = [1, 2, 1]
    result = isPal(L)
    print('Should print True:', result)

# isPalTest()
# silly(5)


#
# Recitation
#

def isPrime(n):
    if n <= 3:
        if n == 2 or n == 3:
            return True
        else:
            return False
    else:
        for divisor in range(2, int(math.sqrt(n))):
            if n % divisor == 0:
                return False
        return True

print(isPrime(30))
