import random
num=random.randint(0,10)
usernum=input("Guess a number between 0 and 10:  ")
userNum=int(usernum)
while userNum!=num:
    if(userNum>num):
        print("Guess Lower")
        usernum=input("Guess a number between 0 and 10:  ")
        userNum=int(usernum)
    elif(userNum<num):
        print("Guess Higher")
        usernum=input("Guess a number between 0 and 10:  ")
        userNum=int(usernum)
    if(userNum==num):
        print("You WIN")
