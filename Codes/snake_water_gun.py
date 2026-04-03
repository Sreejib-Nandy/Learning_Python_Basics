import random

print("Choose 's' for snake , 'w' for water & 'g' for gun")
yourchar = input("Enter your choice : ")
computerchoice = random.choice([-1,0,1])
gamedict = { "s" : -1 , "w" : 0 ,'g' : 1}
yourchoice = gamedict[yourchar]
reversegamedict = { -1 : "Snake", 0 : "Water", 1 : "Gun"}
print(f"You chose {reversegamedict[yourchoice]}")
print(f"Computer chose {reversegamedict[computerchoice]}")

if(computerchoice == yourchoice):
    print("It's Draw")
else :
    if(computerchoice == -1 and yourchoice == 0):
     print("Computer win!")
    elif(computerchoice == -1 and yourchoice == 1):
     print("You win!")
    elif(computerchoice == 0 and yourchoice == -1):
     print("You win!")
    elif(computerchoice == 0 and yourchoice == 1):
     print("Computer win!")
    elif(computerchoice == 1 and yourchoice == -1):
     print("Computer win!")
    elif(computerchoice == 1 and yourchoice == 0):
     print("You win!")
    else:
     print("Something went wrong!")





