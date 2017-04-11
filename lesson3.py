# x = 25
# x = 12345
# epsilon = 0.01
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += 0.00001
#     numGuesses += 1
# print('numGuesses = ', numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print("Failed on square root of", x)
# else:
#     print(ans, "is close to square root of", x)

#Bisection search
# x =0.5
x = float(input("Enter a number: "))
epsilon = 0.01
numGuesses = 0
low = 0.0
high =  max(x,1) if x < 1 else x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print('ans=', ans, ' low=', low, ' high= ', high)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/ 2.0
print('numguesses =', numGuesses)
print(ans, "is close to square root of", x)
