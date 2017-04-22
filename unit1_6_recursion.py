from decimal import *
import random
def keySearch(L, k):
    for elem in L:
        if elem[0] == k: return elem[1]
    return None

EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats': 'mange', 'drinks': 'bois',\
        'likes': 'aime', 1: 'un',\
        '6.00':'6.00'}

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ': # when c isn't a space
            word = word + c # I build a word
        else: # when I find a space
            translation = translation + ' '\
                          + translateWord(word, EtoF) # we translate
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF) #we pass the last word assuming it isn't a space

# print(translate('John eats bread'))
# print(translate('Eric drinks wine'))
# print(translate('Everyone likes 6.00'))
#
def toChars(s):
    # import string
    s = s.lower()
    ans = ''
    for c in s:
        if c.islower():
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1: # if the middle is an odd number
        return True
    else:
        # print("comparing: " + s[0] + " - " + s[-1])
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

# # print(isPalindrome('Guttag'))
# # print(isPalindrome('Guttug'))
# # print(isPalindrome('Able was I ere I saw Elba'))
# print(isPalindrome('Are we not drawn onward, we few, drawn onward to new era?'))
#
def fib(x):
    """assumes x an int >= 0
        Returns Fibonacci of x"""
    assert type(x) == int and x >=  0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        print ('fib of', i, '=', fib(i))


def simpleExp(b, n):
    if n == 0:
        return 1
    else:
        return b * simpleExp(b, n-1)

def Hanoi(n, f, t, s):
    if n == 1:
        print("move from", f, "to", t)
    else:
        Hanoi( n-1, f, s, t)
        Hanoi(1, f, t, s )
        Hanoi(n-1, s, t, f)

#print(Hanoi(5, "f", "t", "s"))

#
# Problem 1
#
# Computes the polynomial function for a given value x. Returns that value.
# Example:
# >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) # f(x) = 7.0x4 + 9.3x3 + 5.0x2
# >>> x = -13
# >>> print evaluate_poly(poly, x) # f(-13) = 7.0(-13)4 + 9.3(-13)3 + 5.0(-13)2
# 180339.9
# poly: tuple of numbers, length > 0
# x: number
# returns: float

# TO DO ...

def Exponent(numerator, exponent):
    if exponent == 1:
        return numerator
    elif exponent == 0:
        return 1
    else:
        return numerator * Exponent(numerator, exponent -1)

def evaluate_poly(poly, x):
    result = 0
    for i in range(len(poly)):
        result += float(poly[i] * Exponent(x, i))
    return result

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
# print(evaluate_poly(poly, x))
#
# Problem 2
#
# Computes and returns the derivative of a polynomial function. If the
# derivative is 0, returns (0.0,).
#
# Example:
# >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
# >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
# (0.0, 35.0, 9.0, 4.0)
#
# poly: tuple of numbers, length > 0
# returns: tuple of numbers
#
# TO DO ...

def Derive(poly, derivative, index):
    if index == len(poly):
        return derivative
    else:
        derivative = derivative + (float( index * poly[index]), )
        return Derive(poly, derivative, index + 1) # **# RETURN as a key word is neccesarry in order to bubble up the bottom function

def compute_deriv(poly):
    derivative = ()
    index = 1
    return Derive(poly, derivative, index)

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)

#
# Problem 3
#
# Uses Newton's method to find and return a root of a polynomial function.
# Returns a tuple containing the root and the number of iterations required
# to get to the root.
#
# Example:
# >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39  derivative = 4x^3 + 9x^2 + 35^x
# >>> x_0 = 0.1
# >>> epsilon = .0001
# >>> print compute_root(poly, x_0, epsilon)
# (0.80679075379635201, 8.0)
#
# poly: tuple of numbers, length > 1.
#      Represents a polynomial function containing at least one real root.
#      The derivative of this polynomial function at x_0 is not 0.
# x_0: float
# epsilon: float > 0
# returns: tuple (float, int)

# (0.0, 35.0, 9.0, 4.0)

def evaluate_derivative(poly, x_0):
    result = 0
    for i in range(len(poly)):
        result += float(poly[i] * Exponent(x_0, i))
    return result

def compute_root(poly, x_0, epsilon):

    numGuesses = 1
    y = evaluate_poly(poly, x_0) # evaluates a polynomial given
    fprimeInput = compute_deriv(poly) # returns a tuple with the derivative
    yprime = evaluate_derivative(fprimeInput, x_0)
    x_1 = x_0 - (y / yprime)

    while abs(x_1 - x_0) >= epsilon * abs(x_1):
        x_0 = x_1
        numGuesses = numGuesses + 1
        y = evaluate_poly(poly, x_0) # evaluates a polynomial given
        fprimeInput = compute_deriv(poly) # returns a tuple with the derivative
        yprime = evaluate_derivative(fprimeInput, x_0) # returns derivative value from the tuple

        x_1 = x_0 - (y / yprime) # Newton's computation
    # print("x_1 diff:", Decimal(abs(x_1 - x_0)), ">=", "x_1 * epsi:", Decimal(epsilon * abs(x_1)))
    return (x_1, numGuesses)

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
# print(Exponent(2, 6))
# print(evaluate_poly(poly, x))
# print("derivative: ", compute_deriv(poly))
# print(compute_root(poly, 0.1, 0.0001))


def load_words():
    inFile = open("words.txt", "r")
    line = inFile.readline()
    wordList = str.split(line)
    return wordList

def choose_word(wordList):
    return   random.choice(wordList)

def eval_letter(letter, _availableLetters):
    if len(letter) > 1 or len(letter) <= 0:
        print("You need to provide only 1 letter")

    if _availableLetters.containing(letter):
        _availableLetters.remove(letter)

    return letter

def place_holder_word(len):
    placeHolder = ""
    for i in range(len):
        placeHolder = placeHolder + "_"
    return placeHolder

def main():
    wordList = load_words()
    wordToGuess = choose_word(wordList)
    placeHolder = place_holder_word(len(wordToGuess))
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    numGuesses = 0
    while numGuesses < 8:
        print("Welcome to the game, Hangman!")
        print("I'm thinking of a word that is", len(wordToGuess), "letters long.")
        print("Available letter:", availableLetters)
        letterToGuess = input("Please guess a letter: ")
        eval_letter(letterToGuess)

#print(choose_word(wordList))
