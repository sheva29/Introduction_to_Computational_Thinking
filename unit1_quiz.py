print("2)")
T = (0.1, 0.1)
x = 0.0
for i in range(len(T)):
    for j in T:
        x += i + j
        print(x)
print(i)
print()


'''
2)  0.1
    0.2
    1.3
    2.4
'''
print("3)")
def f(s):
    print("current s:",s)
    if len(s) <= 1:
        print("return:",s)
        return s
    return f(f(s[1:])) + s[0] #Note double recursion
print(f('math'))
print()

'''
3)  >> atm
    >> hatm
'''

print("4)")
"""assumes: wordList is a list of words in lowercase.
lStr is a str of lowercase letters.
No letter occurs in lStr more than once
returns: a list of all the words in wordList that contain
each of the letters in lStr exactly once and no
letters not in lStr."""
def findAll(wordList, lStr):
    result = []
    letters = sorted(letters)
    for w in wordList:
        w = sorted(w)
        if w == letters:
            result.append(w)
    return result

print()

print("5)")
def f(s, d):
    for k in d.keys():
        d[k] = 0
    for c in s:
        if c in d:
            d[c] += 1
        else: d[c] = 0
    return d

def addUp(d):
    result = 0
    for k in d:
        result += d[k]
    return result

'''
d1 = {}
d2 =  d1 #reference
d1 = f('abbc',d1) > { a: 0, b: 1, c:0}
print addUp(d1) > 1
d2 = f('bbcaa', d2) > {a: 2, b: 2, c:1 }
print addUp(d2) > 5
print f(' ', {}) > {" ": 0}
print result > None

'''
d1 = {}
d2 = d1
d1 = f('abbc', d1)
print(addUp(d1))
d2 = f('bbcaa', d2)
print(addUp(d2))
print(f('', {}))
print(result)
