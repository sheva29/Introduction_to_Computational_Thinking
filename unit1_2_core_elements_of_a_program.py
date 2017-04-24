x = 3
x = x*x
print(x)
y = input('enter a number: ')
print(type(y))
print (y)
y = float(input('enter a number: '))
print (y)

x = int(input('Enter an integer: '))
if x%2 == 0:
    print("Even")
else:
    print("Odd")
    if x%3  != 0:
        print("And not Divisible by 3")

# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ## multiples and ans 3 times for its value
    #print(str(abs(x)) + ' - ans cube:' + str(ans*ans*ans))
    ans = ans + 1
#print 'current guess =', ans
if ans*ans*ans != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))

x = int(input('Enter an integer: '))
for ans in range(0, abs(x) + 1): #range generates a sequence of Integers
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print(x, "It's not a perefect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))

#
# Problem 1
#
# dob = str(input("Enter your date of birth: "))
# lastName = str(input("Enter your last name: "))
# print( lastName + " " +dob)
