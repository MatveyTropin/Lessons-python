import random
points=100
while points>0:
    player_number=int(input("Pick a number from 2 to 12? "))
    if player_number<2 or player_number>12:
        print("Wrong Number!")
        continue
    bid=int(input("hom much will you bet? "))
    if bid>points or bid<1:
        print("Wrong bid!")
        continue
    computer_number=random.randint(2,12)
    print("computer chose " + str(computer_number))
    if player_number==computer_number:
        print("you win jackpot!!!!!!")
        points=points+bid*4
    elif computer_number<7 and player_number<7:
        print("you win your bet!")
        points=points+bid
    elif computer_number>7 and player_number>7:
        print("you win your bet!")
        points=points+bid
    
    else:
        print("you lose your bet!")
        points=points-bid
    print("you have "+str(points)+" points" )
    if points==0:
        print("Game over!!!")
        break
    play=input("do you want to continue?")
    if play=="no":
        print("okey,goodbye!!!")
        break
    