Test = (1,2,3,4,5)
# print(Test[0]) # select them accessing their index
# print(Test[1])

x = 100
divisors = ()
print("divisors size: ", len(divisors))
for i in range(1,x):
    if x % i == 0:
        divisors = divisors+(i,) # by inserting coma, special case

# print("divisors size: ", len(divisors))
# print(divisors)

Techs = ["MIT", "Cal Tech"]
Ivys = ["Harvard", "Yale", "Brown"]
Univs = []
Univs.append(Techs)
# print('Univs', Univs)
#
Univs.append(Ivys)
# print("Univs", Univs)
#
for e in Univs:
    print("e", e)

flat = Techs + Ivys
# print("flat", flat)
#
artsSchools = ["RISD", "Harvard"]
for u2 in artsSchools:
    if u2 in flat:
        flat.remove(u2)
# print("flat", flat)
#
flat.sort()
# print("flat", flat)
#
flat[1] = "UMass"
# print("flat", flat)

L1 = [2]
L2 = [L1, L1]
# print("L2", L2)
L1[0] = 3
# print("L2", L2)
L2[0] = 'a'
# print("L2", L2)
#
L1 = [2]
L2 = L1[:]
# print("L2", L2)
# print('L1', L1)
L2[0] = 'a'
# print('L1', L1)
# print("L2", L2)

def copyList(LSource, LDest):
    for e in LSource:
        LDest.append(e)
        print("LDest", LDest)

L1 = []
L2 = [1,2,3]
copyList(L2, L1)
# print("L1", L1)
# print("L2", L2)
copyList(L1, L1)
# print("L1", L1)

D = { 1: 'one', 'deux':'two', 'pi': 3.14159 }
D1 = D
# print(D1)
D[1] = 'uno'
# print(D1)
for k in D1.keys():
    print(k, "=", D1[k])

EtoF = {"bread": "du pain", "wine": "du vin", "eats": "mange", "drinks": "bois", "likes": "aimes", 1: "un", "6.00": "6.00"}
# print(EtoF)
# print(EtoF.keys())
# print(EtoF.keys)
# del EtoF[1]
# print(EtoF)

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate(sentence):
    translation = ""
    word = ""
    for c in sentence:
        if c != " ":
            word = word + c
        else:
            translation = translation + " "\
                        + translateWord(word, EtoF)
            word = ""
    return translation[1:] + " " + translateWord(word, EtoF)

print(translate("John eats bread"))
print(translate("Steve drinks wine"))
print(translate("John likes 6.00"))
