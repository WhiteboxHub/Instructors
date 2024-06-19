def mygen():
    n =1
    while n<20:
        yield n*n
        n +=1

value = mygen()
for i in value:
    print(i)


def newgen():
    strlen = 10
    EngAlphabets = "abcdefghijklmnopqrstuvwxyz"
    sentence = ""
    def loop():
        nonlocal sentence
        for _ in range(strlen):
            for char in EngAlphabets:
                sentence += char
    loop()
    yield sentence

newsentence = newgen()
for i in newsentence:
    print(i, '\n')
