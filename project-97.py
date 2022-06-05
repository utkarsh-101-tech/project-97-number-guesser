import random

count=0
print("Number guessing game")

randomNo = random.randint(1,9)

while count<5 :
     inputNo =int(input("guess a number between 1 to 9 - "))

     if(inputNo == randomNo):    
        print("You Won")
        break
     elif inputNo > randomNo :
        print("guess was too high")
     else :
        print("guess was too low")
     count+=1

if not count<5 :
    print("You Lose")