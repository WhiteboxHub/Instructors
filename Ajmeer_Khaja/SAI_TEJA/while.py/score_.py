#while program
import random
score = 0
scoreInfo = []
while score<=500:
    scoreValue = random.randint(1,30)
    score = score + scoreValue
    scoreInfo.append(scoreValue)
print('total flips ', len(scoreInfo),scoreInfo,score)
