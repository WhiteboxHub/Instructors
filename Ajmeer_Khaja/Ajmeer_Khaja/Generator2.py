
def CreaingSentence():
    length_of_Sentence = 100;
    engAlphabet = "abcdefghijklmnopqrstuvwxyz"
    TheSentence=""
    mysent = ""
    for i in range(1):
        for j in range(len(engAlphabet)):
            TheSentence = ""
            TheSentence +=engAlphabet[j]
            mysent = TheSentence
            for k in range(len(engAlphabet)):
                TheSentence = mysent
                TheSentence +=engAlphabet[k]
                ksent = TheSentence  
                for l in range(len(engAlphabet)):
                    TheSentence +=engAlphabet[l]

                    # for m in range(len(engAlphabet)):
                    #     TheSentence+=engAlphabet[m]
                    yield TheSentence
                    TheSentence=ksent


thesen = CreaingSentence()

# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
# print(next(thesen))
for i in thesen:
    print(i)
