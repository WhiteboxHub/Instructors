import random

def roll():
    
    min_value=1
    max_value=6
    
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("enter the no of players(2-4) : ")
   
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            print("you can play")
            break
        else:
            print ("enter a valid players in the range")
        
max_score=50
players_score=[0 for _ in range(players)]
while max(players_score)<max_score:
    current_score=0
    should_roll=input("if you want to roll enter(yes): ")
    if should_roll.lower()!="yes":
        break
    value=roll()
    if value==1:
        print("you rolled 1 your turn is over")
        break
        
    else:
        print("you rolled the value:", value)
       
        current_score+=value
    print("your current score is ",current_score)

        

    
