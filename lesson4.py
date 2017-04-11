# Lesson 4

# x =0.5
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(x, 1)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     print('ans =', ans, 'low =', low, 'high= ', high)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/ 2.0
# print('numguesses =', numGuesses)
# print(ans, "is close to square root of", x)


def withinepsilon (x, y, epsilon):
# x,y,epsilon floats. epsilon > 0.0
# returns True if x is within epsilon of y""
    return abs(x - y) <= epsilon

# print(withinepsilon(2,3,1))
# foo = withinepsilon(2,3,0.5)
# print(foo)

def f(x):
    x = x + 1
    print("x =" ,x )
    return x

# x = 3
# z = f(x)
# print("z =", z)
# print("x =", x)

def f1(x):
    def g():
        x = 'abc'
        #assert False
    x = x + 1
    print("x =", x)
    g()
    #assert False
    return x


# x = 3
# z = f1(x)


# Assignment

outstanding_balance = int(input('Enter Outstanding Balance: '))
annual_interest_rate = float(input('Enter Annual Interest Rate: '))


# Problem 1
# Write a program that calculates the credic car d balance after one year
# Minimum monthly payment = .02 x $5000.0 = $100.0
# Interest paid = .18/12.0 x $5000.0 = $75.0
# Principal paid = $100.0 – $75.0 = $25
# Remaining balance = $5000.0 – $25.0 = $4975.0

#minimum_monthly_payment_rate = float(input("Enter Minimum Montly Payement: "))
yearPayment = 0

def calculateCardBalance(balance, interest, payment):

    for x in range(0, 12):
        minimum_monthly_payment = balance * payment
        interest_paid = (interest/12.0) * balance
        principal_paid = minimum_monthly_payment - interest_paid
        balance = balance - principal_paid
        print("month", x)
        print("monthly payment: ", format(round(minimum_monthly_payment, 2)))
        print("outstanding balance: ", format(round(balance, 2)))
        print("principal_paid: ", format(round(principal_paid, 2)))
        print("")

#calculateCardBalance(outstanding_balance, annual_interest_rate, minimum_monthly_payment_rate)


monthlyInterestRate = annual_interest_rate/12

#
# Problem 2
#

def calculateMonthlyPayment(balance):

    monthlyPayment = 0
    while balance > 0:
        print("Balance: ", balance)
        print("monthlyPayment: ", monthlyPayment)

        monthlyPayment += 10
        balance = outstanding_balance
        numMonths = 0

        print("numMonths", numMonths)

        while numMonths < 12 and balance > 0:
            #print("numMonths", numMonths)
            numMonths += 1

            interest = monthlyInterestRate * balance
            #print("interest: ",interest)
            #print("balance before monthly: ", balance)
            balance -= monthlyPayment
            #print("balance after monthly ", balance)
            balance += interest
            #print("balance after interest", balance)
        print("numMonths end: ", numMonths)

    balance = round(balance, 2)

    print("RESULT")
    print("Monthly payment to pay off debt in 1 year: ", monthlyPayment)
    print("Number of Months needed: ", numMonths)
    print("Balance: ", balance)

# calculateMonthlyPayment(outstanding_balance)

def calculateMinMonthlyPayment(balance, yearlyInterest):

    low = balance/12
    high = (balance * (1 + (yearlyInterest/12))** 12) / 12
    monthlyPayment = (high + low)/ 2.0
    epsilon = 0.1
    numGuesses = 0
    monthlyInterest = yearlyInterest/12
    deltaBalance = balance
    numMonths = 0
    # print("high: ", high, "low: ", low)

    while abs(deltaBalance) >= epsilon and monthlyPayment <= high and monthlyPayment >= low:

        numGuesses += 1
        deltaBalance = balance
        numMonths = 0

        while numMonths < 12:

            numMonths += 1
            interest = monthlyInterest * deltaBalance
            deltaBalance -= monthlyPayment
            deltaBalance += interest

        if deltaBalance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment

        monthlyPayment = (high+low)/2.0

    print("RESULT")
    print("Monthly payment to pay off debt in 1 year:  ", deltaBalance)
    print("Number of months needed: ", monthlyPayment)

calculateMinMonthlyPayment(outstanding_balance,annual_interest_rate)
